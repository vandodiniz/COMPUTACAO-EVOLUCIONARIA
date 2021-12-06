# Weasel Program
O 'Weasel Program' é uma experiência feita para demonstrar como uma população de strings pode evoluir até convergir para uma string específica, no caso:

'*ME THINKS IT IS LIKE A WEASEL*'

Esse programa é inspirado no 'teorema do macaco infinito', que diz que um macaco digitando aleatoriamente em um teclado por um intervalo de tempo infinito, eventualmente irá criar qualquer texto desejado, como por exemplo uma obra de William Shakespeare. Entretanto, esse cenário é praticamente impossível, pois a chance do macaco digitar a frase de 29 caracteres que queremos é de 1 em 27^29.

Podemos contornar esse imprevisto com um algoritmo genético computacional, pois além de digitar inúmeros indívuduos de 29 caractes em um velocidade incrivelmente mais rápida, os descendentes estão sujeitos a mutações aleatórias que certamente agilizam ainda mais o objetivo desejado.

O programa gera randomicamente uma string de 29 caracteres e realiza N cópias da mesma. Entretanto, cada cópia possui uma certa chance de mutação em cada um dos caracteres. Feito isso, ele avalia todos os indíviduos da população e seleciona o mais próximo da frase desejada. Ele será a string base para a próxima geração e o processo se repete até que a frase seja alcançada.

Exemplo:

Geração 1: WDLTMNLT DTJBKWIRZREZLMQCO P

Geração 2: WDLTMNLT DTJBSWIRZREZLMQCO L

Geração 10: MDLDMNLS ITJISWHRZREZ MECS L

Geração 20: MELDINLS IT ISWPRKE Z WECSEL

Geração 30: METHINGS IT ISWLIKE B WECSEL

Geração X: METHINKS IT IS LIKE A WEASEL
