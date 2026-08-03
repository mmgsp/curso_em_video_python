# Avaliando Brasileirao

brasileirao = ('Palmeiras', 'Bahia', 'Vasco da Gama', 'Internacional', 'Flamengo', 'Mirassol', 'São Paulo', 'Vitória', 'Corinthians', 'Red Bull Bragantino', 'Grêmio', 'Cruzeiro', 'Botafogo', 'Santos', 'Athletico Paranaense', 'Fluminense', 'Atlético Mineiro', 'Remo', 'Chapecoense', 'Coritiba')

primeiros = brasileirao[:4]
ultimos = brasileirao[16:]
alfabetico = sorted(brasileirao)
chapecoense = brasileirao.index('Chapecoense')+1

print(f'\nTabela: {brasileirao}\n\nPrimeiros Colocados: {primeiros}\n\nÚltimos Colocados: {ultimos}\n\nOrdem Alfabética: {alfabetico}\n\nO Chapecoense está na {chapecoense}ª Posição na tabela.\n')

