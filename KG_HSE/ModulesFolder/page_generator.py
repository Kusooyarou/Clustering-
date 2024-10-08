def generate_html(image_paths, output_path="output.html"):
    html_content = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            flex-basis: 400px;
            max-width: 200%;
            width: 400px; 
            height: 400px; 
            object-fit: cover; /* сохраняет пропорции изображения внутри фиксированного контейнера */
            margin: 10px;
            border: 2px solid #ccc;
            border-radius: 5px;
            transition: transform 0.3s ease;
            }
            img:hover {
                transform: scale(1.05);
                border-color: #666;
            }
            @media (max-width: 768px) {
                img {
                    flex-basis: 45%;
                }
            }
            @media (max-width: 480px) {
                img {
                    flex-basis: 100%;
                }
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
