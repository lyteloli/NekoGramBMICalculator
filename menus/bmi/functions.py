from NekoGram import NekoRouter, Neko, Menu
from aiogram import types
from math import pow

ROUTER = NekoRouter()


@ROUTER.function(name='menu_calculate_bmi_step_2')
async def _(_: Menu, message: types.Message, neko: Neko):
    user_data = await neko.storage.get_user_data(user_id=message.from_user.id)
    weight = int(user_data['menu_calculate_bmi']['text'])
    height = int(user_data['menu_calculate_bmi_step_2']['text'])

    """
    With the metric system, the formula for BMI is weight in kilograms divided by height in meters squared. 
    Since height is commonly measured in centimeters, an alternate calculation formula, dividing the weight 
    in kilograms by the height in centimeters squared, and then multiplying the result by 10,000, can be used.
    """
    bmi = (weight / pow(height, 2)) * 10000

    data = await neko.build_menu(name='bmi_result', obj=message)
    await data.build(text_format={'bmi': bmi})
    await neko.storage.set_user_data(user_id=message.from_user.id)
    await data.send_message()
