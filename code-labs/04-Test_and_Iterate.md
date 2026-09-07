## 4\. Test and Iterate

Before launching the service live, run validation checks in the interactive preview.

1. Open the preview pane inside Google AI Studio.
2. Interact with any navigation buttons, links, or layouts in the preview sandbox to verify the visual experience.
    - **Note on fixing errors**: During generation or testing, you might occasionally face runtime issues or compilation errors. If this happens, AI Studio displays a **Fix** button in the chat, allowing you to ask the agent to automatically diagnose and repair the issue.
   ![Google AI Studio Fix Button Location](https://codelabs.developers.google.com/static/codelabs/cloud-run/images/ai-studio-fix-button.png?authuser=1)
3. If you want to change styling or behavior, instruct the agent through the chat window. For example:
    - `"Could you style the interface using Tailwind CSS, and add a dark mode toggle button?"`
        - `"Include a new section to showcase my recent presentations and talks."`
4. Wait for the agent to update the codebase and check the preview browser to see the updates.
