# Data, Hora e Fuso

## Introdução

O módulo **datetime** é usado para lidar com datas e horas.

```python
import datetime

d = datetime.date(2024,7,3)
print(d)
>>> 2023-07-03
```

O módulo **datetime** está na documentação oficial do Python:  
[Python - Datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)

Temos o objeto *datetime*, que é um único objeto contendo todas as informações de um objeto *date* e um objeto *time*.

```python
import datetime
datetime.datetime(year, month, day, hour, minuto, second, microsecond, tzinfo, *, fold)

data_hora= datetime.datetime(2024, 7, 3, 22, 8)
print(data_hora)
>>> 2024-07-03 22:08:00
```

Temos o método **today()**, que traz a data, hora minutos e segundos do local.

Por fim, podemos ver, também, o méotodo *time()* que traz as informações de hora:

```python
from datetime import time

hora = time(10,20, 0)
print(hora)
>>> 10:20:00
```
## Manipulação de Datas e Horas

Podemos criar e manipular objetos date, time e datetime de várias maneiras, podemos adicionar e subtrair datas, verificar a diferença entre datas etc. Essas manipulações são feitas usando a classe *timedelta*

```python
import datetime

d = datetime.datetime(2024, 7, 3, 22, 15)
print(d)
>>> 2024-07-03 22:15:00
d = d + datetime.timedelta(weeks=1)
print(d)
>>> 2024-07-10 22:15:00
```
Repare que o objeto timedelta representa a duração, a diferença entre duas datas ou horas. No geral, as operações mais comuns são: **adição** ou **subtração** de timedeltas.

Para usar o timedelta, fazemos:

```python

from datetime import datetime, timedelta

data_atual = datetime.now()
tempo_processo = 45
data_estimada = data_atual + timedelta(minutes=tempo_processo)
print(data_estimada)
```

No timedelta, temos que indicar qual unidade de tempo estamos falando (minutos, horas, etc).

Mas repare que não é possível realizar uma operação do tipo **time - timedelta**, pois o timedelta necessita um objeto que tenha o date junto. Para realizar essa operação é necessário, passar um datetime, realizar a operação em horas e extrair só a parte de horas com o time:

```python
resultado = datetime(2024, 7, 4, 18, 12, 00) - timedelta(hours=1)
resultado.time()
```

### Conversão e Formatação de Datas e Horas

Para fazer a conversão de datas e horas usamos:  
* strftime (string format time)
* strptime (string parse time)

Por exemplo:

```python
import datetime

d = datetime.datetime.now()

# Formatando hora e data
print(d.strftime("%d/%m/%Y %H:%M"))
>>> 04/07/2024 18:25

# Convertendo string para datetime
string_data = "04/07/2024 18:26"
d = datetime.datetime.strptime(string_data, "%d/%m/%Y %H:%M")
print(d)
>>> 2024-07-04 18:26:00
```
O **strftime** pode cortar partes do objeto **datetime**, ou seja, podemos exibir apenas o dia/mes, ou dia/mes/ano, ou só as horas. Na documentação, temos todas as opções de máscara, mas podemos ver mais um exemplo:

```python
data_hora_atual = datetime.now()
data_hora_str = "2024-07-04 18:36"
mascara_ptbt = "%d/%m/%Y %a"
print(data_hora_atual.strftime(mascara_ptbt))
>>> 04/07/2024 Thu
