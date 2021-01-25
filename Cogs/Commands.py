import asyncio
import discord 
import bs4
import urllib
import re
import requests
import lxml
from discord.ext import commands
import os
import time
import random
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import json
from urllib import request
from Dtime import Uptime
import platform
import psutil
from ext import cpu

Uptime.uptimeset()
embedcolor = 0xffff33
embederrorcolor = 0xff0000

async def get_id_data():
    with open("announce.json","r") as f:
        channel = json.load(f)
    return channel


class Commands(commands.Cog):

    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            embed=discord.Embed(title=f'환영합니다!',description=f'{member.mention}님이  {member.guild}에 들어오셨습니다. 환영합니다 ! \n현재 서버 인원수: {str(len(member.guild.members))}명',color=embedcolor)
            embed.set_footer(text="환영메시지를 받고싶지 않으시면 봇이 이 채널을 못보게 해주세요")
            embed.set_thumbnail(url=member.avatar_url)
            await member.guild.system_channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            embed=discord.Embed(title=f'안녕히 가세요',description=f'{member.mention}님이  나가셨습니다. 안녕히 가세요 \n현재 서버 인원수: {str(len(member.guild.members))}명',color=embederrorcolor)
            embed.set_footer(text="환영메시지를 받고싶지 않으시면 봇이 이 채널을 못보게 해주세요")
            embed.set_thumbnail(url=member.avatar_url)
            await member.guild.system_channel.send(embed=embed)
        except:
            pass

    @commands.command(name="핑", help="핑을 보여줌")
    async def ping(self, ctx):
        pings = round(self.bot.latency*1000)
        if pings < 100:
            pinglevel = '🔵 매우좋음'
            color=embedcolor
        elif pings < 300: 
            pinglevel = '🟢 양호함'
            color=embedcolor
        elif pings < 400: 
            pinglevel = '🟡 보통'
            color=embedcolor
        elif pings < 6000: 
            pinglevel = '🔴 나쁨'
            color=embederrorcolor
        else: 
            pinglevel = '⚪ 매우나쁨'
            color=embederrorcolor
        embed = discord.Embed(title='핑', description=f'{pings} ms\n{pinglevel}', color=color)
        await ctx.send(embed=embed)

    @commands.command(name="초대", aliases=["초대링크","링크"], help="초대링크를 알려줌")
    async def invite(self, ctx):
        embed=discord.Embed(title="INFINITY봇 링크", color=embedcolor)
        embed.add_field(name="INFINITY 서버초대", value="[서버](https://discord.gg/UByy5cf)", inline=False)
        embed.add_field(name="INFINITY봇 초대", value="[봇(관리자)](https://discord.com/api/oauth2/authorize?client_id=765535083124752394&permissions=8&scope=bot)", inline=False)
        embed.add_field(name="INFINITY봇 초대", value="[봇(최소기능)](https://discord.com/oauth2/authorize?client_id=765535083124752394&scope=bot&permissions=1610607742)", inline=False)
        embed.add_field(name="INFINITY봇 공식홈페이지", value="[밝은테마](http://infinitybot.kro.kr)", inline=False)
        embed.add_field(name="INFINITY봇 공식홈페이지", value="[어두운테마](http://black.infinitybot.kro.kr)", inline=False)
        embed.set_footer(text="이 링크들이 가장 안전해!")
        await ctx.send(embed=embed)

    @commands.command(name="팀원들", help="팀원(?)들 보여줌")
    async def team(self, ctx):
        embed=discord.Embed(title="INFINITY봇 팀원들(?)",color=embedcolor)
        embed.add_field(name="개발자", value="<@!671231351013376015>", inline=False)
        embed.add_field(name="홍보팀", value="<@!689245164383895573>님", inline=False)
        embed.set_footer(text="열심히 일해주셔서 감사합니다!")
        await ctx.send(embed=embed)
    
    @commands.command(name="크레딧", help="도움주신분들 보여줌")
    async def helper(self, ctx):
        embed=discord.Embed(title="크레딧", color=embedcolor)
        embed.add_field(name="도움주신분", value="Team Orora\nreword 님\nminibox님의 PingPongTool 모듈\n곰사냥님 네이버 블로그\nDistube 유튜브", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name="프사", help="프로필사진 보여줌")
    async def profilepicture(self,ctx, *, member:discord.Member=None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f'{member.name} 님의 프사', color=embedcolor)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="DM", aliases = ['dm','디엠'], help="DM을 보냄")
    async def DM(self, ctx, member:discord.Member=None, *, text = None):
        if member == None:
            await ctx.send(f'유저를 멘션해주세요! (예시:.DM {self.bot.user.mention} 내용)')
            return
        if text == None:
            await ctx.send("보낼 내용을 입력해주세요")
            return
        await self.bot.get_user(member.id).send(f'{text}\n`{ctx.author.name}님이 보냄`')
        await ctx.send(f'{member.name}님께 메시지가 전송됐습니다.')

    @commands.command(name="주사위", help="랜덤 주사위값 보여줌")
    async def dice(self, ctx):
        await asyncio.sleep(0.75)
        embed = discord.Embed(title="주사위 굴리는중...", color=embedcolor)
        dice = await ctx.send(embed=embed)
        await asyncio.sleep(0.75)
        embed=discord.Embed(title="랜덤 주사위",description=':game_die: '+ ':one:', color=embedcolor)
        embed1=discord.Embed(title="랜덤 주사위",description=':game_die: '+ ':two:', color=embedcolor)
        embed2=discord.Embed(title="랜덤 주사위",description=':game_die: '+ ':three:', color=embedcolor)
        embed3=discord.Embed(title="랜덤 주사위",description=':game_die: '+ ':four:', color=embedcolor)
        embed4=discord.Embed(title="랜덤 주사위",description=':game_die: '+ ':five:',color=embedcolor)
        embed5=discord.Embed(title="랜덤 주사위",description=':game_die: '+ ':six:', color=embedcolor)
        random_list = [embed, embed1, embed2, embed3, embed4, embed5]
        embed = random.choice(random_list)
        await dice.edit(embed=embed)

    @commands.command(name="정보", aliases=["프로필"], help="유저정보를 보여줌")
    async def information(self, ctx, user:discord.Member=None):
        if user == None:
            user = ctx.author
        status = str(user.status)
        if status == "online":
            status = "온라인🟢"
        elif status == "dnd":
            status = "방해금지⛔"
        elif status == "idle":
            status = "자리비움🟡"
        else:
            status = "오프라인⚪"
        if user.bot == False:
            bot = "유저"
        else:
            bot = "봇"
        try:
            game = str(ctx.author.activities[0].name)
            act = str(ctx.author.activity)
        except:
            game = "없음"
            act = "없음"
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{user.name}의 정보', color=embedcolor)
        embed.add_field(name="이름", value=user.name, inline=False)
        embed.add_field(name="별명", value=user.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=user.id)
        embed.add_field(name="상태", value=f"{status}", inline=False)
        embed.add_field(name="사용자 지정 상태", value=f"{act}", inline=False)
        embed.add_field(name="게임 활동", value=game)
        embed.add_field(name="최상위 역할", value=user.top_role.mention, inline=False)
        embed.add_field(name="봇", value=bot)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="서버정보", help="서버정보 보여줌")
    async def severinfo(self, ctx):
        roles = [role for role in ctx.guild.roles]
        member_count = len(ctx.guild.members)
        only_member_count = len([m for m in ctx.guild.members if not m.bot])
        guild_age = (ctx.message.created_at - ctx.author.guild.created_at).days
        online = len({m.id for m in ctx.author.guild.members if m.status is not discord.Status.offline})
        embed = discord.Embed(title=f'{ctx.guild}의 정보', color=embedcolor)
        embed.add_field(name="서버 이름", value=ctx.guild)
        embed.add_field(name="서버 아이디", value=ctx.guild.id)
        embed.add_field(name="서버 주인", value=f'<@{ctx.guild.owner_id}>', inline=False)
        embed.add_field(name="유저 수(봇포함)", value=member_count)
        embed.add_field(name="유저 수(봇 미포함)", value=only_member_count)
        embed.add_field(name="온라인 유저 수", value=online)
        embed.add_field(name="서버 나이", value=guild_age, inline=False)
        embed.add_field(name="보안 레벨", value=ctx.guild.verification_level)
        embed.add_field(name="서버 위치", value=ctx.guild.region)
        embed.add_field(name="역할 개수", value=len(roles), inline=False)
        embed.add_field(name="이모지 개수", value=len(ctx.guild.emojis))
        embed.add_field(name="부스트 레벨", value=ctx.guild.premium_tier, inline=False)
        embed.add_field(name="부스트 개수", value=ctx.guild.premium_subscription_count)
        embed.add_field(name="규칙 채널", value=ctx.guild.rules_channel, inline=False)
        embed.add_field(name="시스템 채널", value=ctx.guild.system_channel)
        embed.add_field(name="채팅 채널", value=len(ctx.guild.text_channels), inline=False)
        embed.add_field(name="음성 채널", value=len(ctx.guild.voice_channels))
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        await ctx.send(embed=embed)

'''
    @commands.command(name="실1검", help="실시간 검색어 보여줌")
    async def old_search(self, ctx):
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class" : "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i+1))+"위  "+e.text+"\n"
        embed=discord.Embed(title="초록창실검", description= f"{(result)}", color=embedcolor)
        await ctx.send(embed=embed)
'''

    @commands.command(name="실검", aliases = ['실시간검색어'], help="실시간 검색어를 보여줍니다.")
    async def search(self, ctx):
        url="https://datalab.naver.com/keyword/realtimeList.naver?where=main"
        req=urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36 '})
        html=urllib.request.urlopen(req)
        bs=bs4.BeautifulSoup(html, "lxml")
        Time=bs.find('a', {'class': 'time_box _time_trigger'}).find('span', {'class': 'time_txt _title_hms'}).text.strip()
        list_group=bs.find('div', {'class': 'list_group'}).find_all('ul', {'class': 'ranking_list'})
        embed=discord.Embed(description='실시간 검색어', color=embedcolor)
        embed.set_footer(text=f'{Time} 기준')
        rank = 0
        for ranking_list in list_group:
            ranking_item=ranking_list.find_all('li')
            for item in ranking_item:
                rank += 1
                item_title=item.find('span', {'class': 'item_title'}).text.strip()
                ranking_url="https://search.naver.com/search.naver?ie=utf8&query="+item_title.replace(' ', '+')
                embed.add_field(name=f'{rank}위', value=f'[{item_title}]({ranking_url})', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name="따라하기", aliases = ['말하기','말해','따라해'], help="말하면 따라함")
    async def follow(self, ctx, *, followtext=None):
        if followtext == None:
            await ctx.send("따라할 문장을 입력해주세요")
        else:
            await ctx.send(f'{followtext}\n`{ctx.author}님이 시킴`')

    @commands.command(name="건의", aliases = ['오류'], help="건의나 오류 보냄")
    async def errer(self, ctx, *, sendtxt = None):
        if sendtxt == None:
            await ctx.send("보낼 내용을 입력해주세요")
            return
        jin = 671231351013376015
        await self.bot.get_user(jin).send(f'<@!{ctx.author.id}> : {sendtxt}')
        await ctx.send('메시지가 전송됬습니다.')

    @commands.command(name="시간", help="시간 보여줌")
    async def time(self, ctx):
        await ctx.send(embed=discord.Embed(title="지금시간", timestamp=datetime.datetime.utcnow(), color=embedcolor))

    @commands.command(name="계산", help="더하기,빼기,곱하기 계산함")
    async def calc(self,ctx,lan:str=None,first:int=None,second:int=None):
        if first==None or second==None:
            await ctx.send("수를 입력해주세요")
        first=int(first)
        second=int(second)
        if lan=="더하기":
            await ctx.send(first+second)
        elif lan=="빼기":
            await ctx.send(first-second)
        elif lan=="나누기":
            await ctx.send(first/second)
        elif lan=="곱하기":
            await ctx.send(first*second)
        else:
            await ctx.send("더하기,빼기,곱하기 또는 나누기를 입력해주세요")
    
    @commands.cooldown(1, 3, commands.BucketType.user) 
    @commands.command(name="봇정보", help="봇정보 알려줌")
    async def infinitybot_info(self, ctx):
        embed1 = discord.Embed(title="봇정보를 불러오는중입니다....", description="이 작업은 10초정도 걸립니다", color=embedcolor)
        info = await ctx.send(embed=embed1)
        date = datetime.datetime.utcfromtimestamp(((int(self.bot.user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{self.bot.user.name}봇 정보', color=embedcolor)
        embed.add_field(name="이름", value=self.bot.user, inline=False)
        embed.add_field(name="별명", value=self.bot.user.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=self.bot.user.id, inline=False)
        embed.add_field(name="운영체제", value=platform.system())
        embed.add_field(name="운영체제 버젼", value=platform.version())
        embed.add_field(name="프로세스 이름", value=cpu['brand_raw'])
        embed.add_field(name="프로세스 아키텍쳐", value=platform.machine())
        embed.add_field(name="램 크기", value=str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)", inline=False)
        embed.add_field(name="서버 수", value=len(self.bot.guilds))
        embed.add_field(name="유저 수", value=len(self.bot.users))
        embed.add_field(name="개발자", value="jin^^*~#3739")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await info.edit(embed=embed)

    @commands.command()
    async def 공지설정(self, ctx, channel1:discord.TextChannel=None):
        if channel1 == None:
            channel1 = ctx.channel
        guilds = await get_id_data()
        if str(channel1.id) in guilds:
            await ctx.send('이미 공지설정이 등록돼있는 체널입니다.')
        else:
            guilds[ctx.guild.id] = {}
            guilds[ctx.guild.id]['gongji'] = int(channel1.id)
            with open('announce.json', 'w') as f:
                json.dump(guilds, f)
            await ctx.send(f'{ctx.author}님이 <#{channel1.id}>에 공지설정 했습니다.')

    @commands.command(name="개발자", aliases=["developer"], help="개발자를 보여줍니다")
    async def developer(self, ctx):
        await ctx.send("`이 봇의 개발자는 jin^^*~#3739 입니다.\njin^^*~#3739 made this bot.`")
    
    @commands.command(name="하트확인")
    async def _checkvote(self, ctx):
        VOTE = UBPY.UBPYvote(ctx, self.token, bot_id=self.id)
        check = await VOTE.vote()
        if check == True:
            await ctx.send()
        elif check == False:
            print('FALSE')
        else:
            print('ERROR')
 
    @commands.command(name="코로나", help="국내 코로나 상황")
    async def corona(self, ctx):
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        datecr = soup.find('span', {'class': 't_date'})
        totalcovid = soup.select('dd.ca_value')[0].text
        todaytotalcovid = soup.select('p.inner_value')[0].text
        todaydomecovid = soup.select('p.inner_value')[1].text
        todayforecovid = soup.select('p.inner_value')[2].text
        totalca = soup.select('dd.ca_value')[2].text
        todayca = soup.select('span.txt_ntc')[0].text
        totalcaing = soup.select('dd.ca_value')[4].text
        todaycaing = soup.select('span.txt_ntc')[1].text
        totaldead = soup.select('dd.ca_value')[6].text
        todaydead = soup.select('span.txt_ntc')[2].text
        embed = discord.Embed(title='코로나19 국내 발생현황', color=embedcolor, url='http://ncov.mohw.go.kr/')
        embed.add_field(name='확진자', value=f'{totalcovid}({todaytotalcovid})명\n국내발생: {todaydomecovid} 명\n해외유입: {todayforecovid} 명', inline=False)
        embed.add_field(name='격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
        embed.add_field(name='격리해제', value=f'{totalca}({todayca}) 명', inline=False)
        embed.add_field(name='사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
        embed.set_footer(text=datecr.string)
        await ctx.send(embed=embed)

    @commands.command(name="업타임", help="업타인을 확인합니다")
    async def uptime(self, ctx):
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        embed=discord.Embed(title="인피니티봇 업타임", description=f"{hours}시간 {minitues}분 {seconds}초 가동됬습니다", color=embedcolor)
        await ctx.send(embed=embed)

    @commands.command(name="giveawaystart", aliases=["gstart","기부시작"], help="기부를 시작합니다")
    async def gstart(self, ctx, mins:int, *, prize:str):
        embed=discord.Embed(title="Giveaway!", color=embedcolor)
        embed.add_field(name=f"상품 : {prize}", value=f"호스트 : {ctx.author.mention}")
        end=datetime.datetime.utcnow() + datetime.timedelta(seconds=mins*60)
        embed.add_field(name="끝나는 시간", value=f"{end} UTC")
        embed.set_footer(text=f"{mins} 뒤에 끝납니다")
        msg=await ctx.send(embed=embed)
        await msg.add_reaction("🎉")
        await asyncio.sleep(mins)
        new_msg=await ctx.channel.fetch_message(msg.id)
        users=await new_msg.reaction[0].users().flatten()
        users.pop(users.index(bot.user))
        winner=random.choice(users)
        await ctx.send(f"축하합니다! {winner.mention}님이 우승하였습니다!")

    @commands.command(name="help", aliases=["도움","도움말"], help="도움말 표시")
    async def help_command(self, ctx, func=None):
        if func is None:
            embed = discord.Embed(title="INFINITY Bot 도움말", description="접두사는 `.` 입니다.", color=embedcolor)
            cog_list = ["Commands","Economy","Management","Music","Chat"]
            for x in cog_list:
                cog_data = self.bot.get_cog(x)
                command_list = cog_data.get_commands()
                embed.add_field(name=x, value=" ".join([c.name for c in command_list]), inline=True)
            await ctx.send(embed=embed)
        else:
            command_notfound = True
            for _title, cog in self.bot.cogs.items():
                if not command_notfound:
                    break
                else:
                    for title in cog.get_commands():
                        if title.name == func:
                            cmd = self.bot.get_command(title.name)
                            embed = discord.Embed(title=f"명령어 : {cmd}", description=cmd.help, color=embedcolor)
                            embed.add_field(name="사용법", value=cmd.usage)
                            await ctx.send(embed=embed)
                            command_notfound = False
                            break
                        else:
                            command_notfound = True

    @commands.command(name="소개", aliases=['info'])
    async def so_gea(self, ctx):
        embed=discord.Embed(title="디스코드 인피니티봇 소개", color=embedcolor)
        embed.add_field(name="접두사는 `.`이고 `.도움`으로 명령어를 알아보세요", value="놀이,경제,관리 기능등 잡기능이 많은 봇입니다")
        embed.add_field(name="인피니티봇 많이 이용해주세요^^", value="[인피니티봇 서버링크](https://discord.gg/UByy5cf) \n[인피니티봇 초대링크(관리자)](http://invite.admin.infinitybot.kro.kr) \n[인피니티봇 초대링크(최소기능)](http://invite.infinitybot.kro.kr)", inline = False)
        embed.set_footer(text="공지채널에 .공지설정 해주시면 감사하겠습니다.")
        await ctx.send(embed=embed) 
    
    @commands.command(name="한강", help="한강 수온 확인")
    async def han_river(self, ctx):
        text=["힘들면 잠시 쉬세요","당신이 있어서 행복합니다","당신은 소중합니다","한번만 더 생각해보세요"]
        text=random.choice(text)
        json = requests.get('http://hangang.dkserver.wo.tc/').json()
        temp = json.get("temp")
        time = json.get("time")
        embed = discord.Embed(title='💧 한강온도', colour=embedcolor)
        embed.add_field(name=f"{temp}°C", value=f"{time}에 측정됌", inline=False)
        embed.add_field(name=f"{text}", value="위기상담전화 ☎1577-0199")
        await ctx.send(embed=embed)

    @commands.command(name="e학습터공지", aliases=["이학습터공지"], help="e학습터 공지를 보여줍니다")
    async def cls_edunet(self, ctx):
        try:
            webpage = requests.get("https://cls1.edunet.net/cyber/cm/mcom/pmco000b00.do")
            soup = BeautifulSoup(webpage.content, "html.parser")
            find = soup.find('div', {'class':'m-txt img'})
            imgURL = find.find('img')['src']
            embed=discord.Embed(title="e학습터 알림", color=embedcolor)
            embed.set_image(url=imgURL)
            embed.set_footer(text="서울 기준입니다")
            await ctx.send(embed=embed)
        except:
            return await ctx.send("e학습터 사진공지가 없습니다")

    @commands.cooldown(1, 1, commands.BucketType.user) 
    @commands.command(name="날씨", help="날씨를 보여줍니다")
    async def weather(self, ctx, *, location:str=None):
        if location == None:
            location = "서울"
        try:
            html = requests.get(f'https://search.naver.com/search.naver?&query=%EB%82%A0%EC%94%A8+{location}')
            soup = BeautifulSoup(html.text, 'html.parser')
            find_address = soup.find('span', {'class':'btn_select'}).text
            find_temp = soup.find('span',{'class': 'todaytemp'}).text
            find_weather = soup.find('p', {'class':'cast_txt'}).text
            find_dust = soup.find('span', {'class':'num'}).text
            embed=discord.Embed(title=f"{location}의 날씨정보", color=embedcolor)
            embed.add_field(name=f"현재온도 : {find_temp}", value=find_weather)
            embed.add_field(name="미세먼지", value=find_dust)
            embed.set_footer(text=f"{find_address}기준")
            await ctx.send(embed=embed)
        except:
            await ctx.send("그런 위치는 없어요")

    @commands.command(name="이더리움", aliases=["ETH"], help="이더리움 시세 보여드립니다")
    async def eth(self, ctx):
        html = requests.get("https://coinmarketcap.com/currencies/ethereum/")
        soup = BeautifulSoup(html.text, 'html.parser')
        price = soup.find('td').text
        change = soup.find('p',{'class': 'sc-1eb5slv-0 sc-1siv958-1 jnWaEv'}).text
        embed=discord.Embed(title="이더리움 가격", color=embedcolor)
        embed.add_field(name="가격", value=price)
        embed.add_field(name="변동률", value=change)
        await ctx.send(embed=embed)

    @commands.command(name="상메", help="자신이나 다른사람의 상태메시지를 보여줍니다")
    async def status(self, ctx, m: discord.Member=None):
        if m == None:
            m = ctx.author
        status = str(m.status)
        if status == "online":
            status = "온라인🟢"
        elif status == "dnd":
            status = "방해금지⛔"
        elif status == "idle":
            status = "자리비움🟡"
        else:
            status = "오프라인⚪"
        acts = m.activities
        act = [i for i in acts if isinstance(i, discord.CustomActivity)]
        if act:
            act = act[0]
        else:
            return await ctx.send("상메가 없습니다\n오프라인일 경우 상메가 없다고 나옵니다")
        text = act.name
        if text:
            embed=discord.Embed(title=f"{m.name}의 상테메시지", color=embedcolor)
            embed.add_field(name=f"{text}", value=f"{status}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("상메가 없습니다")

    @commands.command(name="주소검색", aliases=["주소"], help="정확한 주소를 보여줍니다")
    async def address(self, ctx, *, keyword:str=None):
        if keyword == None:
            return await ctx.send("키워드를 입력해주세요\n예시: .주소검색 합정 스타벅스")
        else:
            try:
                url = f'https://dapi.kakao.com/v2/local/search/keyword.json?query={keyword}'
                headers = {"Authorization": "KakaoAK ㅁㄴㅇㄹ"}
                name = requests.get(url, headers = headers).json()['documents'][0]['place_name']
                address = requests.get(url, headers = headers).json()['documents'][0]['address_name']
                phone = requests.get(url, headers = headers).json()['documents'][0]['phone']
                road_address = requests.get(url, headers = headers).json()['documents'][0]['road_address_name']
                category = requests.get(url, headers = headers).json()['documents'][0]['category_group_name']
                if phone == "":
                    phone = "없음"
                if address == "":
                    address = "없음"
                if road_address == "":
                    road_address = "없음"
                if category == "":
                    category = "없음"
                embed=discord.Embed(title=f"{keyword} 검색결과", color=embedcolor)
                embed.add_field(name="이름", value=name, inline=False)
                embed.add_field(name="주소", value=address)
                embed.add_field(name="도로명주소", value=road_address)
                embed.add_field(name="전화번호", value=phone, inline=False)
                embed.add_field(name="종류", value=category)
                await ctx.send(embed=embed)
            except:
                await ctx.send("오류가 발생했어요")                

    @commands.command(name="이름번역", help="이름을 영어로 번역합니다")
    async def name_trans(self, ctx, name:str=None):
        if name == None:
            return await ctx.send("이름을 입력해주세요")
        else:
            client_id = "ㅁㄴㅇㄹ"
            client_secret = "ㅁㄴㅇㄹ"
            encText = urllib.parse.quote(name)
            url = f"https://openapi.naver.com/v1/krdict/romanization?query={encText}"
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode==200):
                response_body = response.read()
                json_dict = json.loads(response_body.decode('utf-8'))
                result = json_dict['aResult'][0]
                name_items = result['aItems']
                print(name_items)
                names = [name_item['name'] for name_item in name_items]
                embed=discord.Embed(title=f"{name}의 번역결과", color=embedcolor)
                embed.add_field(name=names, value="정확한 결과는 아닙니다.")
                await ctx.send(embed=embed)
            else:
                print("Error Code:" + rescode)

    @commands.command(name="서버확인", help="관리자용 명령어입니다")
    async def tttttest(self, ctx):
        if ctx.author.id == 671231351013376015:
            list1 = self.bot.guilds[0]
            names = [list1['name'] for list1 in name]
            with open("guilds.txt", 'w', -1, "utf-8") as a:
                a.write(str(names))
            file1 = discord.File("guilds.txt")
            await ctx.author.send(file=file1)
            os.remove("guilds.txt")
        else:
            await ctx.send("봇 개발자만 가능해여")
  
def setup(bot):
    bot.add_cog(Commands(bot))
print("Commands")
