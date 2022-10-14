# Este programa tem o intuito de calcular de forma simples a emissão de CO2 anual de uma empresa, sem considerar
# a emissão nos processos produtivos.

meta = float(input('Insira a meta anual de emissão de CO2 em Toneladas de CO²: '))
resma = int(input('Quantas resmas de papel são utilizadas anualmente? (1 resma = 500 folhas) \n'))
elet = float(input('Qual é o gasto com energia elétrica anualmente em R$? \n'))
kwh = float(input('Qual é o preço médio do kWh em R$? \n'))
comb = float(input('Qual é o gasto com combustível anualmente em R$? \n'))
tipocomb = int(input('''Qual é o tipo de combustível utilizado?
        1 para Gasolina
        2 para Etanol
        3 para Diesel
        4 para GNV
            '''))
precocomb = float(input('Qual é o preço médio do combustível em R$? \n'))
voo = int(input('Quantos voos são feitos anualmente? (Consideramos que cada voo percorra 1000km) \n'))

# Cálculo para a emissão x gasto de papel. Cada resma de papel produz em média 3,5kg CO2.
# Vale dizer que a cultura de Eucalipto, árvore utilizada na produção de papel não compensa a emissão de carbono,
# uma vez que a produção de cada resma gasta em média 100.000 litros de água e 5.000 kWh de energia elétrica.

papel = resma * 3.5

# Cálculo para a emissão x gasto em energia elétrica. Emissão de kg CO2 por kWh.

estimativae = (elet / kwh) * 0.090

# Cálculos para a emissão pelo combustível.
# (Para a GASOLINA: Litros de combustível * Densidade do Combustível * Taxa de Presença de Álcool * Taxa de
#  Transformação do Combustível em CO2).
# (Para o ÁLCOOL: Para efeitos práticos é considerado que o álcool tem emissão ZERO. O desenvolvimento da
# cana-de-açúcar consome o CO2 emitido pela combustão do álcool na (aproximadamente) mesma proporção).
# (Para o DIESEL: Litros de combustível * Densidade do Combustível * Taxa de Transformação do Combustível em CO2).
# (Para o GNV: Há variação na porcentagem que se considera a diminuição da emissão de CO2 pelo GNV em relação ao
# diesel que vão de 15% a 20%. Para efeitos deste trabalho consideraremos 18%.

estimativac = 0
if tipocomb == 1:
    estimativac = ((comb / precocomb) * 0.75 * 0.78 * 2.8)
elif tipocomb == 2:
    estimativac = 0
elif tipocomb == 3:
    estimativac = ((comb / precocomb) * 0.83 * 3.2)
elif tipocomb == 4:
    estimativac = (((comb / precocomb) * 0.83 * 3.2) / 100) * 82
else:
    print('Opção inválida, tente novamente!')

# Cálculos para a emissão pelos voos realizados.
# Nos utilizamos da ferramenta Google Flights para obter emissões de voos reais por passageiro.
# Neste trabalho vamos considerar 85kg CO2 como o valor emitido num voo de 1000km por passageiro.

estimativav = voo * 85

# Cálculos conclusivos.

print('-' * 40)

emissao = (papel + estimativae + estimativac + estimativav) / 1000
print(f'Neste ano a sua empresa produziu {emissao:.2f} Toneladas de CO².')

# Análise dos resultados.

if (emissao == meta) or (emissao < meta):
    print('''Parabéns, Sua meta foi atingida! Continue a atuar de forma consciente e a aplicar soluções
inteligentes e eficientes no seu negócio.''')
else:
    print(f'Ainda faltam {emissao - meta:.2f} Toneladas de CO² para atingir sua meta.')
    print('''Sua empresa precisa encontrar formas inteligentes e estratégias direcionadas para reduzir os parâmetros
que mais contribuem para a elevação dos índices de emissão, como vôos e combustível.''')

print('-' * 40)

# Neutralização do carbono. Infos.

print(f'''A compensação também é fundamental para amortizar nossa pegada de carbono no mundo. Neste sentido, a cada 7
árvores plantadas aproximadamente 1 tonelada de CO² é absorvida durante os seus primeiros 20 anos de desenvolvimento.
Para aplicarmos este conceito ao seu negócio, uma conta bem simples deve ser feita: multiplicamos o total de CO² 
emitidos pela sua empresa por 7. Portanto, {(emissao // 1) * 7} árvores serão necessárias para neutralizar a emissão
de carbono.''')

print('-' * 40)

# Neutralização do carbono. Calculadora.
# Neste trabalho foi utilizado o Jatobá como referência de árvore a ser plantada. Em consulta a sites de venda de
# sementes colhemos a informação de que cada 250g contam com apx. 63 sementes ao custo de R$115.

print(f'''Após a neutralização ser atingida, cada tonelada de CO² absorvido a mais lhe rende 1 crédito de carbono
que equivale a aproximadamente R$17. Estime a seguir o quanto você poderia lucrar a partir do investimento em 
redução de carbono, considerando que já possua a quantidade de terras necessárias para acomodar o plantio: ''')
print('''Utilizaremos o Jatobá, com custo de R$460 por quilo de sementes.
5''')
invest = float(input('Insira o valor R$ que você gostaria de investir: '))
plantio = int((invest / 460) * 252) // 1
toneladas = (plantio / 7) // 1
rendimento = toneladas * 21.05
print(f'\n Seu investimento renderá {plantio} árvores, que em 20 anos sequestrarão {toneladas} T CO² -eq.')
print(f'''O ganho bruto será de R${rendimento:.2f} enquanto seu lucro será de R${rendimento - invest:.2f} com o ativo
a R$17, registrando {((rendimento - invest) / invest) * 100:.2f}% de rendimento em 20 anos.
''')
print(f'''Vale lembrar que os Créditos de Carbono possuem um potencial gigantesco de valorização no Brasil, portanto
o lucro poderia ser muito maior! Na Europa o valor de cada crédito já chegou em €57, que equivale a R$286,51.''')
