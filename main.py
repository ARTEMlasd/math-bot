import logging
from aiogram import Bot, Dispatcher, types, executor
from utils import get_square_of_triangle_gerone, romb, get_square_of_circle, quadratic_equation, validate_input


import kb
# Устанавливаем уровень логов на INFO, чтобы видеть сообщения о действиях бота
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token='6175397043:AAHnr5JbCbHoLBvt6TWBNo6GoSiQSPbVqi0')
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(msg):
    await msg.reply(
        "я решаю некоторые (уравнения,примеры). Команда:/help, если не знаешь какие команды есть в этом боте ")

@dp.message_handler(commands=['help'])
async def send_welcome(msg):
    await msg.reply("fiuty",reply_markup=kb.markup3)

command = None

# Обработчик всех остальных сообщений
@dp.message_handler(commands=['S_круга'])
async def echo_message(msg):
    global command
    command = 'Площадь_круга'
    await msg.reply("Скинь радиус если мозгов хватит")


@dp.message_handler(commands=['Discriminant'])
async def echo_message(msg):
    global command
    command = 'Дискриминант'
    await msg.reply("Скинь кофиценты, через запятую, пример(a, b, c (заместо букв свои цифры) надеюсь до тебя дошло, если ты не сможешь скинуть даже это,(Молчу про решение уравнения), то обратись в садик)")


@dp.message_handler(commands=['S_Треугольника'])
async def echo_message(msg):
    global command
    command = 'Площадь_треугольника'
    await msg.reply("Скинь размеры каждой стороны треугольника, через запятую, пример(a, b, c (заместо букв свои цифры) надеюсь до тебя дошло, если ты не сможешь скинуть даже это,(Молчу про нахождение, треугольника всего лишь через две формулы), то обратись в садик)")

@dp.message_handler(commands=['S_Ромба'])
async def echo_message(msg):
    global command
    command = 'Площадь_площадь'
    await msg.reply("скинь размеры диагоналий d1 и d2")

@dp.message_handler()
async def send_welcome(msg):
    global command


    if command == 'Площадь_треугольника':
        commands = validate_input(msg.text)
        if commands == False:
            await msg.answer('неправильные данные')
        else:
            r = get_square_of_triangle_gerone(commands[0], commands[1], commands[2])
            await msg.answer(str(r))
    if command == 'Дискриминант':
        commands = validate_input(msg.text)
        if commands == False:
            await msg.answer('неправильные данные')
        else:
            x = quadratic_equation(commands[0],commands[1], commands[2])
            await msg.answer(str(x))
    if command == 'Площадь_круга':
        commands = validate_input(msg.text)
        if commands == False:
            await msg.answer('неправильные данные')
        else:
            r = get_square_of_circle(int(commands[0]))
            await msg.answer(str(r))
    if command == 'Площадь_Ромба':
        commands = validate_input(msg.text)

        r = romb(int(commands[0]), int(commands[1]))
        await msg.answer(str(r))


executor.start_polling(dp, skip_updates=True)
