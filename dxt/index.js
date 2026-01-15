#!/usr/bin/env node
/**
 * Node.js wrapper for Google Automation MCP server
 * Spawns the Python MCP server and pipes stdio for MCP communication
 */

import { spawn } from "child_process";
import { platform } from "os";

const isWindows = platform() === "win32";

/**
 * Try to spawn the MCP server using various methods
 */
function trySpawnServer() {
  // Methods to try in order of preference
  const methods = [
    // 1. uvx (recommended - handles venv automatically)
    { cmd: "uvx", args: ["google-automation-mcp"] },
    // 2. pipx run
    { cmd: "pipx", args: ["run", "google-automation-mcp"] },
    // 3. Direct command (if installed globally or in PATH)
    { cmd: "google-automation-mcp", args: [] },
    // 4. Python module
    { cmd: "python3", args: ["-m", "google_automation_mcp"] },
    { cmd: "python", args: ["-m", "google_automation_mcp"] },
  ];

  for (const method of methods) {
    try {
      const proc = spawn(method.cmd, method.args, {
        stdio: ["pipe", "pipe", "pipe"],
        shell: isWindows,
        env: {
          ...process.env,
          PYTHONUNBUFFERED: "1",
        },
      });

      // Check if spawn succeeded by waiting briefly for early errors
      let spawnFailed = false;
      proc.on("error", () => {
        spawnFailed = true;
      });

      // Give it a moment to fail if command doesn't exist
      if (!spawnFailed && proc.pid) {
        return proc;
      }
    } catch {
      // Try next method
      continue;
    }
  }

  return null;
}

/**
 * Main entry point
 */
function main() {
  const server = trySpawnServer();

  if (!server) {
    const errorMsg = JSON.stringify({
      jsonrpc: "2.0",
      error: {
        code: -32603,
        message:
          "Failed to start Google Automation MCP server. Please install it with: pip install google-automation-mcp",
      },
      id: null,
    });
    process.stdout.write(errorMsg + "\n");
    process.exit(1);
  }

  // Pipe stdin to server
  process.stdin.pipe(server.stdin);

  // Pipe server stdout to our stdout (MCP messages)
  server.stdout.pipe(process.stdout);

  // Forward stderr for debugging
  server.stderr.on("data", (data) => {
    process.stderr.write(data);
  });

  // Handle server exit
  server.on("close", (code) => {
    process.exit(code ?? 0);
  });

  // Handle our own exit
  process.on("SIGINT", () => {
    server.kill("SIGINT");
  });

  process.on("SIGTERM", () => {
    server.kill("SIGTERM");
  });

  // Handle errors
  server.on("error", (err) => {
    const errorMsg = JSON.stringify({
      jsonrpc: "2.0",
      error: {
        code: -32603,
        message: `Server error: ${err.message}`,
      },
      id: null,
    });
    process.stdout.write(errorMsg + "\n");
    process.exit(1);
  });
}

main();
