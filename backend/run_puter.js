// backend/run_puter.js
import fs from "fs";
import puter from "puter-js";

// Get text file path from Python subprocess
const args = process.argv.slice(2);
const filePath = args[0];

// Read text content
const text = fs.readFileSync(filePath, "utf8");

(async () => {
  try {
    // Run AI query
    const response = await puter.ai.chat(
      `Classify the following documentation into Sink, Source, or Sanitizer issues and describe possible vulnerabilities:\n\n${text}`,
      { model: "gpt-5-nano" }
    );

    // Print it — VERY important!
    console.log(response);
  } catch (err) {
    console.error("Error in run_puter.js:", err);
  }
})();
