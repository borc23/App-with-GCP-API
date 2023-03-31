# S**imple app using GCP API**
## **About**
Wanted to make a simple app where I use GCP API to find similar image URLs based on the image URL provided by you.

## **How to get a GCP API key**

1. Sign in to your **Google Cloud account**. If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads .
2. Install the **Google Cloud CLI** .
3. Create or select a **Google Cloud project** .
4. Make sure that **billing is enabled** for your Cloud project .
5. Enable the **API Keys API** 
7. Go to the **Google Cloud Console**.
8. In the target GCP Project, go to **APIs & Services > Credentials**.
9. Click **Create credentials**, then select **API key** from the menu.
10. The API key created dialog displays the string for your newly created key. Copy your key string and keep it secure .

That's it! You now have a GCP API key. 😊

### *Changes in the code*

Replace: 
```python
api_key = 'YOUR_API_KEY'
```
With your API key obtained in the *Google Cloud Account*.

## Program

Running on http://127.0.0.1:5000

![First page](img/Screenshot%202023-03-31%20201006.png)
![Input Image](img/Boston-Terrier-8.jpg)
![Result page](img/Screenshot%202023-03-31%20201024.png)
![Result page](img/Boston-Terrier-Temperament-long.jpg)