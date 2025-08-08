import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
    
def montar_Html(html_content, messages, link, type):
    for cont in range(len(messages[type])):
       html_content = html_content.replace(f"{{msg{cont + 1}}}", messages[type][cont])
    html_content = html_content.replace(
        "{link}",
        f'''<a href="{link}" style="color: #f3f3f3; padding: 16px 13%" class="color-button">Acompanhar Solicitação</a>'''
    )
    return html_content
    
def send_email(manager, solicitacion, subject, title, receiver_email, link, html_content, type):

    # Informações necessárias para o envio do e-mail
    sender_email = "ronyelison78@gmail.com"
    sender_password = "" # Use uma senha de app para Gmail
    messages = [[f'Prezado(a) {manager},',
                f'Encaminho para sua apreciação a documentação referente à funcionalidade <span class="purple">{title}</span> do <span class="purple">GIT.flow</span>. ',
                'Solicito, por gentileza, a revisão e <span class="purple">aprovação</span> do conteúdo. Caso identifique a necessidade de ajustes, estou à disposição para realizá-los.',
                f'A solicitação foi feita por: <span class="purple">{solicitacion}</span>.',
                f''],
                 

            [f'Prezado(a) {solicitacion},',
                f'Após análise da documentação referente à funcionalidade <span class="purple">{title}</span> do <span class="purple">GIT.flow</span>.',
                'Identificamos que o material ainda necessita de alguns <span class="purple">ajustes</span> para estar em conformidade com os padrões técnicos e de clareza esperados.',
                'Assim que a versão ajustada estiver pronta, por favor, nos encaminhe para nova avaliação.',
                ''],
                

            ['Prezados(as),',
                f'Informamos que a documentação referente à funcionalidade <span class="purple">{title}</span> foi revisada, aprovada e já está publicada em nosso repositório oficial do <span class="purple">GIT.flow</span>.',
                'Este material faz parte do conjunto de guias técnicos da plataforma e tem como objetivo <span class="purple">orientar</span> o uso correto da funcionalidade, promovendo padronização e eficiência nos processos.',
                'A documentação está disponível no botão abaixo, solicitamos que todos os envolvidos consultem o material conforme necessário.',
                '']
        ]

    """Envia um e-mail com conteúdo HTML."""
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Trocar as mensagens {msg1}, {msg2}, ... e o {link} no conteúdo HTML
    html_content = montar_Html(html_content, messages, link, type)

    # Anexar o conteúdo HTML
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Configurar o servidor SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Identificar-se para o servidor SMTP
        server.starttls()  # Iniciar conexão segura
        server.login(sender_email, sender_password)

        # Enviar e-mail
        server.send_message(msg)
        print("E-mail enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")

    finally:
        server.quit()

if __name__ == "__main__":
    # Ler o arquivo HTML
    html_content = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Guaraves</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            
            body {
                font-family: calibri, sans-serif;
                margin: 0 auto;
                background-color: #f4f4f4;
                font-size: 1.125rem; 
                letter-spacing: 0.5px;
                width: 50%;
            }

            #colorbox {
                background-color: #9d00a0c7;
                color: white;
                padding:  1.25rem; 
                text-align: center;
                border-top-right-radius: 1.25rem;
                border-top-left-radius: 1.25rem;
                margin-top: 1rem;
            }

            #content {
                padding: 1.25rem;
                
            }

            #colorbox p{
                opacity: 0.5;
            }

            #colorbox h1 {
                font-weight: 600;
            }

            #content h4{
                background: #8c8c8c29;
                border-left: 6px solid #9d00a0c7;
                border-top-right-radius: 12px;
                border-bottom-right-radius: 12px;
                padding: 24px;
                margin: 40px auto;
                max-width: 1400px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                text-align: left;
                font-weight: 400;
                opacity: 0.75;
            }

            .purple {
                color: #9d00a0c7;
                text-decoration: none;
            }

            #content p {
                line-height: 1.6;
                font-size: 1.25rem;
            }

            #button-container {
                text-align: center;
                margin: 3rem 0;
                width: 100%;
            }

            .color-button {
                background-color: #9d00a0c7;
                color: #f3f3f3;
                border: none;
                padding: 1rem 1.4rem;
                border-radius: 0.3rem;
                cursor: pointer;
                font-size: 1rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin: 0 auto;
                transition: 0.4s ease;
                text-decoration: none;
                width: 25%;
            }

            .color-button:hover {
                background-color: #8c00a0c7;
            }

            #finally {
                padding: 1.25rem;
                font-size: 1.25rem;
                line-height: 1.6;
            }
            </style>
        </head>

        <body>
            <div id="colorbox">
                <h1>GIT.flow</h1>
                <p>Confirmação de Cadastro</p>
            </div>
            <div id="content">
                <h4>Solicitação criada com sucesso!</h4>
                <p>{msg1}
                    <br><br>
                    {msg2}
                    <br><br>
                    {msg3}
                    <br><br>
                    {msg4}
                </p>
            </div>
            <div id="button-container">
                {link}
            </div>
            <div id="finally">
                <p>Atenciosamente,</p>
                <span class="purple">Equipe GIT.flow</span>
            </div>
        </body>
        </html>'''

    # Enviar o e-mail
    send_email("Wedson",
                "Richarlyson",
                "Aprovação de Documentação",
                "Checar Documentação",  
                "gabriel.nunes@guaraves.com.br",
                "google.com",
                html_content,
                1
                )
