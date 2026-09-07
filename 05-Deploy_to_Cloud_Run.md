## 5\. Deploy to Cloud Run

Once your prototype is fully functional, deploy it as a public service on Cloud Run.

1. In the top-right corner of Google AI Studio, click the **Publish** button to initiate the deployment wizard.![Google AI Studio Publish Button Location](https://codelabs.developers.google.com/static/codelabs/cloud-run/images/ai-studio-publish-button.png?authuser=1)
2. Click **Get Started** to configure your Google Cloud project.
    - Verify the target **Google Cloud Project** drop-down matches the project you associated with your workspace.
        - AI Studio will automatically generate a unique service identifier for the Cloud Run instance.
        - Optionally, you can specify a custom `.ai.studio` URL prefix (e.g., `your-portfolio-name.ai.studio`) as part of your deployment configuration.
3. If this is your first time deploying and you are using standard Google Cloud parameters, you may be prompted to specify an organization type and supply billing details.
4. Click **Publish App**.
5. The container build, container registration, and service deployment steps happen in the background. This process normally completes in 2–4 minutes.
6. When deployment finishes, copy the generated **App URL** and visit the live application link in a browser tab.
7. Test the live web application in your browser!
