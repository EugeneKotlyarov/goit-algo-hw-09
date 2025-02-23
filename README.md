# Жадібні алгоритми та динамічне програмування

## опис

Це домашнє завдання включає в себе реалізацію двох алгоритмів для визначення найкращого способу видачі решти: жадібного алгоритму та алгоритму динамічного програмування.

## Жадібний алгоритм

`find_coins_greedy` бере цілу суму грошей і повертає словник із кількістю монет кожного номіналу, використаних для формування цієї суми. Алгоритм завжди вибирає монету найвищого номіналу, яка не перевищує суму, що залишилася.

## Алгоритм динамічного програмування

`find_min_coins` також отримує цілу суму грошей і повертає словник із мінімальною кількістю монет, необхідних для компенсації цієї суми. Алгоритм створює таблицю для зберігання мінімальної кількості монет, необхідних для всіх сум від 0 до заданої суми, а потім повертається назад, щоб знайти комбінацію монет.

## Порівняння продуктивності

Ми порівняли продуктивність двох алгоритмів для таких варіантів решти: `[10400, 12332, -5346, 4234, 1204, 5555]`, вимірявши час їх виконання. Результати в монетах в наших випадках завжди виявились однаковими, хоча теорія підказує, що Жадібний не завжди може знайти оптимальне рішення. По часу виконання Жабідний відпрацьовує на 3-4 порядки швидше.
Нижче наведено результати:

|   | Решта | Монети | Час |
| --- | --- | --- | --- |
| Жабідний | 10400 | {50: 208} | 0.000002 | 
| Дин.прогр. | 10400 | {50: 208} | 0.003303 | 
| --- |  |  |  |
| Жабідний | 12332 | {50: 246, 25: 1, 5: 1, 2: 1} | 0.000001 | 
| Дин.прогр. | 12332 | {50: 246, 25: 1, 5: 1, 2: 1} | 0.003780 | 
| --- |  |  |  |
| Жабідний | 4234 | {50: 84, 25: 1, 5: 1, 2: 2 | 0.000001 | 
| Дин.прогр. | 4234 | {50: 84, 25: 1, 5: 1, 2: 2 | 0.001262 | 
| --- |  |  |  |
| Жабідний | 1204 | {50: 24, 2: 2} | 0.000000| 
| Дин.прогр. | 1204 | 50: 24, 2: 2} | 0.000338 | 
| --- |  |  |  |
| Жабідний | 5555 | {50: 111, 5: 1} | 0.000001 | 
| Дин.прогр. | 5555 | {50: 111, 5: 1} | 0.001682 | 

## Висновок

Жадібний алгоритм швидкий і простий, але в теорії не завжди може бути оптимальним.
