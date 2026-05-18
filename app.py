from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Սահմանում ենք նկարի հղումը (կարող եք դնել ցանկացած նկարի URL)
    image_url = "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?q=80&w=500"
    
    # Ձեր GitHub-ի կամ ցանկացած այլ կայքի հղումը
    website_url = "https://ofelyakirakosyan19-pixel.github.io/lab8-cicd/" 

    # Կառուցում ենք HTML-ը
    html_content = f"""
    <div style="text-align: center; font-family: Arial, sans-serif; margin-top: 50px;">
        <h1>Welcome to CI/CD Project!</h1>
        <p>Powered by Containerized Automation & Scalable Pipelines</p>
        
        <div style="margin: 20px 0;">
            <img src="{image_url}" alt="DevOps" style="border-radius: 10px; max-width: 100%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
        </div>
        
        <p>
            <a href="{website_url}" target="_blank" style="padding: 10px 20px; background-color: #24292e; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
                Visit My GitHub Profile
            </a>
        </p>
    </div>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
