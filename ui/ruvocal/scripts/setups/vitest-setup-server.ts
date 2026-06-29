import { vi, afterAll } from "vitest";
import dotenv from "dotenv";
import { resolve } from "path";
import fs from "fs";

// Load the .env file
const envPath = resolve(__dirname, "../../.env");
const envLocalPath = resolve(__dirname, "../../.env.local");

let envVars = {};

if (fs.existsSync(envPath)) {
	dotenv.config({ path: envPath });
	const envContent = fs.readFileSync(envPath, "utf-8");
	envVars = { ...envVars, ...dotenv.parse(envContent) };
}

if (fs.existsSync(envLocalPath)) {
	dotenv.config({ path: envLocalPath });
	const envContent = fs.readFileSync(envLocalPath, "utf-8");
	envVars = { ...envVars, ...dotenv.parse(envContent) };
}

// Separate public and private variables
const publicEnv = {};
const privateEnv = {};

for (const [key, value] of Object.entries(envVars)) {
	if (key.startsWith("PUBLIC_")) {
		publicEnv[key] = value;
	} else {
		privateEnv[key] = value;
	}
}

vi.mock("$env/dynamic/public", () => ({
	env: publicEnv,
}));

vi.mock("$env/dynamic/private", async () => {
	return {
		env: {
			...privateEnv,
			// RVF store uses in-memory for tests (no file path = no persistence)
			RVF_DB_PATH: "",
		},
	};
});

afterAll(async () => {
	// No cleanup needed — RVF store is in-memory for tests
});
