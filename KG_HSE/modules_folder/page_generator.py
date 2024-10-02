def generate_html(image_paths, output_path="output.html"):
    html_content = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                margin: 0;
                padding: 0;
                background: rgb(153, 50, 204);
                background: linear-gradient(90deg, rgba(153, 50, 204, 1) 0%, rgba(138, 43, 226, 1) 50%, rgba(75, 0, 130, 1) 100%);

            }
            img {
                max-width: 100%;
                height: auto;
                margin: 5px;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
    """
    
    for image_path in image_paths:
        html_content += f'<img src="{image_path}" alt="Image">\n'
    
    html_content += """
    </body>
    </html>
    """
    
    with open(output_path, "w") as f:
        f.write(html_content)