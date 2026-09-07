## 6\. (OPTIONAL) Add a custom domain

By default, Cloud Run hosts your service on a Google-managed `run.app` subdomain. If you want to use a personal domain (like `yourname.com` or `portfolio.yourname.com`), you can map a custom domain to your service.

### Step 0: Add a domain mapping in Cloud Run

1. Go to the [Cloud Run Domain Mappings](https://console.cloud.google.com/run/domains?authuser=1) page in the Google Cloud Console.
2. Click **Add Mapping**.
3. Choose the Cloud Run service you want to map from the drop-down.
4. Input your custom domain name (for example, `yourname.com` or `portfolio.yourname.com`).
5. Click **Next** or **Continue**. Cloud Run will display the DNS records (such as `A` / `AAAA` or `CNAME` records) that you must create with your domain registrar.

### Step 2: Configure your DNS registrar

1. Sign in to your domain registrar's administration panel (for example, Squarespace, GoDaddy, or Namecheap).
2. Open the DNS management or DNS settings configuration page for your domain.
3. Create the DNS records matching the values shown in the Cloud Run mapping wizard:
    - For apex domain mappings (e.g., `yourname.com`), add the listed `A` and `AAAA` records.
        - For subdomain mappings (e.g., `portfolio.yourname.com`), add the listed `CNAME` record.
4. Save the DNS configuration changes.

### Step 3: Wait for SSL certificate provisioning

Once the DNS changes propagate:

1. Google Cloud will automatically provision a managed SSL/TLS certificate for your secure connection.
2. This process usually completes in about 15 minutes but can take up to 24 hours depending on DNS propagation.
3. Once completed, your custom domain will route safely to your portfolio website.
