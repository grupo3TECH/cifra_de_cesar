import PySimpleGUI as sg

nome = sg.popup_get_text("Qual seu nome? ", title="Vamos nos conhecer!", text_color = 'black', background_color = 'RoyalBlue', location = (500,250))
sg.popup(f"Olá {nome}, você sabe o que é cifra de cesar? \nÉ um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, A seria substituído por D, B se tornaria E, e assim por diante.", title="Boas Vindas!", text_color = 'black', background_color = 'RoyalBlue', location = (500,250))

frase = sg.popup_get_text("OBS: Não utilizar caracteres especiais. \nPor gentileza, digite a frase: ", title="Escolha uma frase!",text_color = 'black', background_color = 'RoyalBlue', location = (500,250)).upper()
fraseFormatadaArray = list(frase)

chave = int(sg.popup_get_text("Digite a chave para encriptação: ", title="Escolha da chave.", text_color = 'black', background_color = 'RoyalBlue', location = (500,250)))

escolha = int(sg.popup_get_text("Deseja encriptar ou decriptar sua mensagem? \nDigite 1 para encriptar; \nDigite 2 para decriptar;", title="Eis a questão...", text_color = 'black', background_color = 'RoyalBlue', location = (500,250)))

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '] #Como convertemos toda a frase para letras em maiúsculo podemos definir somente as letras em maiúsculo do alfabeto

fraseConvertidaArray = []

if 0 < chave < 26:
    if escolha == 1:
        
        for i in fraseFormatadaArray:
            posicao = alfabeto.index(i)
            if i == ' ':
                nova_Posicao = posicao
            else:
                nova_Posicao = posicao + chave
            caractere_criptografado = alfabeto[nova_Posicao % len(alfabeto)]
            fraseConvertidaArray.append(caractere_criptografado)
            fraseImpressaUsuario = ''.join(fraseConvertidaArray).lower()

        sg.popup("Sua frase encriptada é: ", fraseImpressaUsuario, title="Encriptada", text_color = 'black', background_color = 'RoyalBlue', location = (500,250))
      
    elif escolha == 2:
        
        for i in fraseFormatadaArray:
            posicao = alfabeto.index(i)
            if i == ' ':
                nova_Posicao = posicao
            else:
                nova_Posicao = posicao - chave
            caractere_decriptado = alfabeto[nova_Posicao % len(alfabeto)]
            fraseConvertidaArray.append(caractere_decriptado)
            fraseImpressaUsuario = ''.join(fraseConvertidaArray).lower()
        sg.popup("Sua frase decriptada é: ", fraseImpressaUsuario, title="Decriptada", text_color = 'black', background_color = 'RoyalBlue', location = (500,250))

    else:
        
        sg.popup_error("Você deve digitar uma opção válida!", title="Inválido", text_color = 'black', background_color = 'Crimson', location = (500,250))
       
else:
    
    sg.popup_error("A chave digitada não é válida. Escolha valores entre 0 e 26.", title="Inválido", text_color = 'black', background_color = 'Crimson', location = (500,250))


    


