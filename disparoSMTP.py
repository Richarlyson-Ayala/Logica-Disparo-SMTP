import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def ler_Arquivo(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def send_email(solicitacion, receiver_email, subject, link, html_content, type, manager, title):
    sender_email = "ronyelison78@gmail.com"
    sender_password = "szkh qyun cnvj uotq" # Use uma senha de app para Gmail
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

    for cont in range(len(messages[type])):
       html_content = html_content.replace(f"{{msg{cont + 1}}}", messages[type][cont])
       if cont == 4:
            html_content = html_content.replace(
                "{link}",
                f'''<a href="{link}" 
                    style="background-color:#9d00a0c7;color:#f3f3f3;border:none;padding:1rem 1.4rem;
                    border-radius:0.3rem;cursor:pointer;font-size:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.1);
                    margin:0 auto;text-decoration:none;display:inline-block;widht:50%;transition:0.4s ease;"
                >Acompanhar Solicitação</a>'''
            )

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
    html_content = ler_Arquivo("index.html")

    # Enviar o e-mail
    send_email("Rony", "gabriel.nunes@guaraves.com.br", "Testando Email", "google.com", html_content, 2, "Rodrigo", "Checar páginas")