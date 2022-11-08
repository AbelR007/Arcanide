import discord
from discord.ext import commands
from chars import chars, void_chars
import autolist

class SwitchForm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = False
    
    @discord.ui.button(
        label = "Void Form",
        style = discord.ButtonStyle.green
    )
    async def switch_form(self, interaction: discord.Interaction, button: discord.ui.Button):
        # await interaction.response.edit_message(embed = embed)
        self.value = True
        self.stop()

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.hybrid_command(
        name="types",
        description="Lists all the types of pokemon",
    )
    async def types(self, ctx: commands.Context):
        embed = discord.Embed(
            title = "Types of Characters",
            description = f"""
            Fire
            Water
            Earth
            Electric
            Psychic
            Light
            Dark
            Techno
            """
        )
        await ctx.send(embed = embed)

    @commands.hybrid_command(
        name = "info",
        description = "Displays information about the character",
        aliases = ['i']
    )
    async def info_command(self, ctx: commands.Context, char: str) -> None:

        # char_name = 'luna'
        char_name = char
        chars_list = chars['char']
        char_name = autolist.autocorrect(char_name, chars_list)
        char_no = chars_list.index(char_name)

        char_id = chars['charid'][char_no]
        void_form = chars['void_form'][char_no]
        char_type = chars['type'][char_no]
        char_rarity = chars['rarity'][char_no]
        char_desc = chars['desc'][char_no]
        imgurl = chars['imgurl'][char_no]

        health = chars['health'][char_no]
        attack = chars['attack'][char_no]
        defense = chars['defense'][char_no]
        range_attack = chars['range_attack'][char_no]
        range_defense = chars['range_defense'][char_no]
        speed = chars['speed'][char_no]

        move1 = chars['moves'][char_no][0]
        move2 = chars['moves'][char_no][1]
        move3 = chars['moves'][char_no][2]
        move4 = chars['moves'][char_no][3]

        embed = discord.Embed(
            title = f"{char_name.title()} #{char_id}",
            description = f"*{char_desc}*",
            color = discord.Color.purple()
        )
        embed.add_field(
            name = "Void Form",
            value = f"{void_form.title()} #{char_id}",
            inline = True
        )
        embed.add_field(
            name = "Type",
            value = f"{char_type.title()}",
            inline = True
        )
        embed.add_field(
            name = "Rarity",
            value = f"{char_rarity.title()}",
            inline = True
        )

        embed.add_field(
            name= "Base Stats",
            value=f"""
                **Health**: {health}
                **Attack**: {attack}
                **Defense**: {defense}
            """,
            inline = True
        )
        embed.add_field(
            name = "\u2800",
            value = f"""
                **Range Attack**: {range_attack}
                **Range Defense**: {range_defense}
                **Speed**: {speed}
           """,
            inline = True
        )
        embed.add_field(
            name = "Moves",
            value = f"{move1} | {move2} | {move3} | {move4}",
            inline = False
        )

        embed.set_thumbnail(
            url = f"{imgurl}"
        )
        embed.set_author(
            name = "⭐⭐⭐"
        )
        # view = SwitchForm()
        msg = await ctx.send(embed = embed)
    
    @commands.hybrid_command(
        name = "voidinfo",
        description = "Information about the Void Form Characters",
        aliases = ['vi'],
    )
    async def void_info_command(self, ctx, *, char: str) -> None:

        char_name = char
        void_chars_list = void_chars['char']
        print(char_name, void_chars_list)
        char_name = autolist.autocorrect(char_name, void_chars_list)
        print(char_name)
        char_no = void_chars_list.index(char_name)

        char_id = void_chars['charid'][char_no]
        base_form = void_chars['base_form'][char_no]
        char_type = void_chars['type'][char_no]
        char_rarity = chars['rarity'][char_no]
        char_desc = chars['desc'][char_no]
        imgurl = void_chars['imgurl'][char_no]

        health = void_chars['health'][char_no]
        attack = void_chars['attack'][char_no]
        defense = void_chars['defense'][char_no]
        range_attack = void_chars['range_attack'][char_no]
        range_defense = void_chars['range_defense'][char_no]
        speed = void_chars['speed'][char_no]

        move1 = void_chars['moves'][char_no][0]
        move2 = void_chars['moves'][char_no][1]
        move3 = void_chars['moves'][char_no][2]
        move4 = void_chars['moves'][char_no][3]
        
        void_embed = discord.Embed(
            title=f"{char_name.title()} #{char_id}V",
            description=f"*{char_desc}*",
            color=discord.Color.purple()
        )
        void_embed.add_field(
            name="Void Form",
            value=f"{base_form.title()} #{char_id}",
            inline=True
        )
        void_embed.add_field(
            name="Type",
            value=f"{char_type.title()}",
            inline=True
        )
        void_embed.add_field(
            name="Rarity",
            value=f"{char_rarity.title()}",
            inline=True
        )

        void_embed.add_field(
            name="Base Stats",
            value=f"""
                **Health**: {health}
                **Attack**: {attack}
                **Defense**: {defense}
            """,
            inline=True
        )
        void_embed.add_field(
            name="\u2800",
            value=f"""
                **Range Attack**: {range_attack}
                **Range Defense**: {range_defense}
                **Speed**: {speed}
           """,
            inline=True
        )
        void_embed.add_field(
            name="Moves",
            value=f"{move1} | {move2} | {move3} | {move4}",
            inline=False
        )

        void_embed.set_thumbnail(
            url=f"{imgurl}"
        )
        void_embed.set_author(
            name="⭐⭐⭐"
        )
        await ctx.send(embed = void_embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))
