def get_html_head_for_mail() -> str:
    """
    Return the <head> in html format
    """
    return """
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <style>
                body {
                    font-family: "Lato", Arial, sans-serif;
                    background-color: #e8e8ea;
                    margin: 0;
                    padding: 0;
                    color: #5a5a5a;
                }
                .email-container {
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    text-align: center;
                    border-collapse: collapse;
                    border-radius: 15px; /* Rounded edges for the container */
                }
                .header {
                    /* background-color: #121c45; */
                    border-top-left-radius: 15px; /* Rounded edges for the header */
                    border-top-right-radius: 15px; /* Rounded edges for the header */
                }
                .header td {
                    padding: 0;
                    border-spacing: 0;
                }
                .header td table {
                    width: 100%;
                    background-color: #121c45;
                    border-radius: 15px 15px 0px 0px;
                    border-collapse: collapse;
                }
                .footer {
                    border-bottom-left-radius: 15px; /* Rounded edges for the footer */
                    border-bottom-right-radius: 15px; /* Rounded edges for the footer */
                }
                .footer td {
                    border-top: 1px solid #e0e0e0;
                    font-size: 12px;
                }
                .header img {
                    width: 100px;
                    height: auto;
                }
                .content {
                    padding: 40px 20px;
                    line-height: 1.5;
                    background-color: #ffffff;
                    color: #12182d;
                }
                a.button {
                    background-color: #ad89dc;
                    color: #ffffff !important;
                    padding: 10px 20px;
                    margin: 25px auto;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 4px;

                }
                a.button:hover {
                    background: linear-gradient(90deg, #ac96e0 0%, #7ea5e6 42.88%);
                }
            </style>
        </head>
    """


def get_html_content_header():
    return """
        <tr class="header">
            <td>
                <table>
                    <tbody>
                        <td>
                            <img src="https://bi360.com.co/assets/icon-bi360.png" alt="BI360" />
                        </td>
                    </tbody>
                </table>
            </td>
        </tr>
    """


def get_html_content_footer():
    return """
        <tr class="footer">
            <td>
                <p>
                    Si no solicitaste un restablecimiento de contraseña, por favor ignora este correo.
                    <br />
                    © 2023 BI 360. Todos los derechos reservados.
                </p>
            </td>
        </tr>
    """


def build_html_for_mail(title: str, body: str) -> str:
    return f"""
        <!DOCTYPE html>
        <html lang="es">
            {get_html_head_for_mail()}
            <body>
                <table class="email-container">
                    {get_html_content_header()}
                    <tr class="content">
                        <td>
                            <h1 style="color: #0a0f26">{title}</h1>
                            {body}
                        </td>
                    </tr>
                    {get_html_content_footer()}
                </table>
            </body>
        </html>
    """
