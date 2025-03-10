from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler, CallbackQueryHandler, JobQueue, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from uuid import uuid4
import time, datetime
from re import search, sub
from uuid import uuid4
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#lista = ['Moon1997', 'crepeer1497', 'vikypediaVA', 'Calbe', 'elah900', 'Lord_Possum', 'Franci02', 'enricomestieri', 'kalef_pa', 'Gufo_Laborioso', 'LucaQuelloFigo', 'Sulfrum', 'serewow20', 'Rupto', 'Zinzo90', 'Ghouler', 'ThisisGus', 'Mushrambo', 'CantKilleanTheZilean', 'GasterTheSkeleton', 'ciaozombi', 'darkbatu', 'CharlesY', 'sEdivad', 'TheTrash', 'Pornopat', 'giumar', 'Giuchi96', 'inusO', 'Bilbolo', 'Stroke2', 'Manfano', 'dvd2000', 'julesontheedge', 'ErenBlaze', 'Ducatistanato', 'Charmei', 'FrancoFre', 'C_0000FF', 'jakolo', 'Nav_1', 'Darkfire99', 'Tirannosauro123', 'Sammuelpaz', 'xAgumoNx', 'Fulgar', 'mifaisonno', 'Apinya', 'Stansot930', 'Pipp93', 'Carlovan', 'MadWhichOfNord', 'Shari_8', 'Daenaera', 'Wallflower96', 'Monnncy', 'Crepeer', 'Ragyflex', 'Pietrodocks', 'danyy666', 'sburroesplosivo', 'Allen_is_life', 'It1707', 'Alessio278', 'drugle91', 'RLabel', 'Icecraft5', 'palby', 'LamantiGatto', 'BlackShadow_77', 'Lar4_B', 'Antonelloo', 'MadDiscordia410', 'vincitoracci', 'Lore_Manga', 'Shawking', 'mattia_mayta', 'ABauglir', 'LuluxAurelianus', 'MMteo02', 'Pera46', 'MrKabom', 'UsernameForTelegram', 'DaviniSuperBao', 'Alex9cento', 'Masterkeyblade0', 'DarkJack22', 'Congioo', 'Dunedan', 'JuansJB', 'Raukonar', 'Deb95', 'L_ucienCheEntra', 'I3z4h3l', 'JoK3R90', 'ale183', 'iam94', 'Tsubu', 'JustValex', 'oz_il_gvande_e_tevvibile', 'cedvis', 'Heeze', 'Mallox', 'solid40', 'ChiariSan', 'TheOfficialSeba', 'Trik16', 'EdEddEddie', 'Lellollul', 'Samael99', 'RobertoBlandini', 'Tequila01', 'XdemetraX', 'Jh0Pans', 'JayJouker22', 'Mazinga93', 'hhhbhhhk', 'HyperN02', 'Agente3001', 'MassiveDynamic', 'Masky39', 'Aeris00', 'GabryMuzio', 'Il_Tanzo', 'Rombeta', 'nonmirompereicoglioni', 'P4r1d3', 'Cuntadin', 'NicoStreet', 'TrumpKun', 'IltuoUsername2', 'MattIsHereBitches', 'HeilHitler10', 'juve1minecraft', 'CH4R124RD', 'MattyScorpion', 'Ilianbright', 'gunnyX', 'Valerios94', 'eapiova', 'Testa_di_culo', 'CICCIO_PASTICCI0', 'ZeroEscapeIsTheBest', 'iesaiemdecau', 'Meeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'Miky_cy', 'Giopsss', 'BastonLigio', 'Mat8071', 'DeViLPaNDaa', 'BlueStitch', 'riccardo1357', 'Shiroesama', 'Gionny001', 'Attila33', 'Greg_redWOLF', 'SuperAlessio', 'GiackAloZ', 'Truccatore', 'bMaioz', 'Yamiki', 'Paletto', 'Gabbo86', 'JonnyMiche', 'ChildOfEden', 'Mastro_Geppetto', 'merrhause', 'LorenzoDeG', 'AralePanaleECambiaIlCanale', 'BlackCondor', 'kibiror', 'Brusacod', 'Prezzemolo', 'ErenKyojin', 'isy99', 'ecodallaluna', 'Envy_Harbringer', 'Eugenio53390', 'The_SeSS_Boss', 'PitX98', 'Giuliabaldacci', 'MiracleBlade1', 'Sciscio', 'Gsjsjsbd', 'pollonio', 'Buz_gIo', 'Ewk95', 'AleVampire17', 'Ludovica15', 'harduini', 'BennyCarota', 'EliaNeri', 'gabrielekeko', 'Sweetchxxs', 'Enree', 'Kurumis', 'AngelaKet', 'luch94', 'OneFuckingDollar', 'Dantemcray', 'GioRonchi', 'MichelaCossu', 'Acuo95']
#lista = ['moon1997', 'crepeer1497', 'vikypediava', 'calbe', 'elah900', 'lord_possum', 'franci02', 'enricomestieri', 'kalef_pa', 'gufo_laborioso', 'lucaquellofigo', 'sulfrum', 'serewow20', 'rupto', 'zinzo90', 'ghouler', 'thisisgus', 'mushrambo', 'cantkilleanthezilean', 'gastertheskeleton', 'ciaozombi', 'darkbatu', 'charlesy', 'sedivad', 'thetrash', 'pornopat', 'giumar', 'giuchi96', 'inuso', 'bilbolo', 'stroke2', 'manfano', 'dvd2000', 'julesontheedge', 'erenblaze', 'ducatistanato', 'charmei', 'francofre', 'c_0000ff', 'jakolo', 'nav_1', 'darkfire99', 'tirannosauro123', 'sammuelpaz', 'xagumonx', 'fulgar', 'mifaisonno', 'apinya', 'stansot930', 'pipp93', 'carlovan', 'madwhichofnord', 'shari_8', 'daenaera', 'wallflower96', 'monnncy', 'crepeer', 'ragyflex', 'pietrodocks', 'danyy666', 'sburroesplosivo', 'allen_is_life', 'it1707', 'alessio278', 'drugle91', 'rlabel', 'icecraft5', 'palby', 'lamantigatto', 'blackshadow_77', 'lar4_b', 'antonelloo', 'maddiscordia410', 'vincitoracci', 'lore_manga', 'shawking', 'mattia_mayta', 'abauglir', 'luluxaurelianus', 'mmteo02', 'pera46', 'mrkabom', 'usernamefortelegram', 'davinisuperbao', 'alex9cento', 'masterkeyblade0', 'darkjack22', 'congioo', 'dunedan', 'juansjb', 'raukonar', 'deb95', 'l_uciencheentra', 'i3z4h3l', 'jok3r90', 'ale183', 'iam94', 'tsubu', 'justvalex', 'oz_il_gvande_e_tevvibile', 'cedvis', 'heeze', 'mallox', 'solid40', 'chiarisan', 'theofficialseba', 'trik16', 'ededdeddie', 'lellollul', 'samael99', 'robertoblandini', 'tequila01', 'xdemetrax', 'jh0pans', 'jayjouker22', 'mazinga93', 'hhhbhhhk', 'hypern02', 'agente3001', 'massivedynamic', 'masky39', 'aeris00', 'gabrymuzio', 'il_tanzo', 'rombeta', 'nonmirompereicoglioni', 'p4r1d3', 'cuntadin', 'nicostreet', 'trumpkun', 'iltuousername2', 'mattisherebitches', 'heilhitler10', 'juve1minecraft', 'ch4r124rd', 'mattyscorpion', 'ilianbright', 'gunnyx', 'valerios94', 'eapiova', 'testa_di_culo', 'ciccio_pasticci0', 'zeroescapeisthebest', 'iesaiemdecau', 'meeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'miky_cy', 'giopsss', 'bastonligio', 'mat8071', 'devilpandaa', 'bluestitch', 'riccardo1357', 'shiroesama', 'gionny001', 'attila33', 'greg_redwolf', 'superalessio', 'giackaloz', 'truccatore', 'bmaioz', 'yamiki', 'paletto', 'gabbo86', 'jonnymiche', 'childofeden', 'mastro_geppetto', 'merrhause', 'lorenzodeg', 'aralepanaleecambiailcanale', 'blackcondor', 'kibiror', 'brusacod', 'prezzemolo', 'erenkyojin', 'isy99', 'ecodallaluna', 'envy_harbringer', 'eugenio53390', 'the_sess_boss', 'pitx98', 'giuliabaldacci', 'miracleblade1', 'sciscio', 'gsjsjsbd', 'pollonio', 'buz_gio', 'ewk95', 'alevampire17', 'ludovica15', 'harduini', 'bennycarota', 'elianeri', 'gabrielekeko', 'sweetchxxs', 'enree', 'kurumis', 'angelaket', 'luch94', 'onefuckingdollar', 'dantemcray', 'gioronchi', 'michelacossu', 'acuo95']

aste = dict()
status = dict()
id_gruppo = (-1001087161580, 0)
id_admin = (25571068, 0)
canale = -1001099221374
#CANALE TEST -1001135376115
link_gruppo = "https://t.me/joinchat/AYYu_EDMxOyMgLFIAQtISA"
url_ch = "https://t.me/+QYTJfrwZMqTvq1NH"


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	pass
	#update.message.reply_text('Benvenuto nell\'AntiMes bot!')

def help(bot, update):
	pass
	#update.message.reply_text('Usa /cerca @username per vedere se Ã¨ nel mes :)')
	
def log(name, user_id, action, temp):
	f = open("log.txt", "a")
	f.write(name+' ('+str(user_id)+') '+action+' ['+temp+']\r\n')
	f.close()
	
def link_user(user):
	if user == '-':
		return user
	text = '<a href="t.me/'+user+'">'+user+'</a>'
	return text
	
def getTime(temp):
	res = int(temp-time.time())
	m = str(res//60)
	s = str(res-int(m)*60)
	if len(s) == 1:
		s = '0'+s
	return m+':'+s
	
def chiudi(bot, update, job_queue):
	global status
	date = str(datetime.datetime.now().date())+' '+ str(time.strftime('%H:%M:%S'))
	

	if update != 'job':
		if not update.message.from_user.id in id_admin:
			return
		try:
			bot.deleteMessage(canale, status['canale'])
		except:
			pass
		for j in job_queue.jobs():
			if j.name == 'asta':
				j.schedule_removal()
		
	testo = 'Asta di '+link_user(status['user'])+" <b>[TERMINATA]</b>\n\n<b>"+status['testo']+"</b>\n\nVincitore: "+link_user(status['offerente'][-1])+'\nOfferta finale: <b>'+str(status['offerta'][-1])+' monete</b>' #Offerente: -\nOfferta attuale: -\nScadenza: 5 minuti"
	bot.editMessageText(text=testo, chat_id=status['chat'],message_id=status['id'], parse_mode='HTML', disable_web_page_preview=True)
	bot.deleteMessage(status['chat'], status['tag_msg'])
	try:
		bot.editMessageText(chat_id=canale, message_id=status['canale'], text=testo, parse_mode='HTML', disable_web_page_preview=True)
	except:
		pass
	if status['chat'] < 0:
		#bot.unpinChatMessage(status['chat'])
		try:
			f = open('pin.txt', 'r')
			r = int(f.read())
			bot.pinChatMessage(status['chat'], r, disable_notification=True)
		except:
			bot.sendMessage(25571068, 'Nessun messaggio da fissare!')
	if status['offerta'][-1] == 1:
		bot.sendMessage(status['chat'], '@'+status['offerente'][-1]+', hai vinto l\'asta per "'+status['testo']+'".\n\nDai <b>'+str(status['offerta'][-1])+' moneta</b> a @'+status['user']+'.', parse_mode='HTML')
	else:
		bot.sendMessage(status['chat'], '@'+status['offerente'][-1]+', hai vinto l\'asta per "'+status['testo']+'".\n\nDai <b>'+str(status['offerta'][-1])+' monete</b> a @'+status['user']+'.', parse_mode='HTML')
	bot.sendMessage(175104816, 'asta finita')
	log(status['user'], '', "- asta \""+status['testo']+"\" terminata! Vincitore: "+status['offerente'][-1]+", offerta: "+str(status['offerta'][-1]), date)
	status = dict()
	
def del_sondaggio(bot, job):
	global aste
	try:
		bot.deleteMessage(canale, aste[str(job.context[1])]['canale'])
		bot.deleteMessage(job.context[0], job.context[1])
	except:
		pass
	try:
		aste.pop(str(aste[str(job.context[1])]['canale']))
		aste.pop(str(job.context[1]))
	except:
		pass
	
def timer_sond(bot, job):
	global aste
	date = str(datetime.datetime.now().date())+' '+ str(time.strftime('%H:%M:%S'))
	message_id = str(job.context[1])
	try:
		if aste[message_id]['time'] <= time.time():
			del_sondaggio(bot, job)
			job.schedule_removal()
			return
	except:
		print("Exception in timer_sond")
		job.schedule_removal()
	
	if int(search('[0-9]+:([0-9]+)', getTime(aste[message_id]['time'])).group(1)) % 30 == 0:
		likes = ''
		for n in aste[message_id]['like']:
			likes += '\n'+link_user(n)
			
		n_like = len(aste[message_id]['like'])
		if n_like == 0:
			n_like = ''
		else:
			n_like = ' '+str(n_like)
		
		keyboard = [[InlineKeyboardButton(chr(128077)+n_like, callback_data='like'), InlineKeyboardButton(chr(10060), callback_data='elimina')],
				[InlineKeyboardButton(chr(128317), callback_data='uppa'), InlineKeyboardButton("Crea asta", callback_data='crea')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		
		ch_key = [[InlineKeyboardButton(chr(128077)+n_like, callback_data='like'), InlineKeyboardButton('Gruppo', url=link_gruppo)]]
		reply_markup_ch = InlineKeyboardMarkup(ch_key)
		
		text = "Sondaggio di "+link_user(aste[message_id]['user'])+" [<b>"+getTime(aste[message_id]['time'])+"</b>]\n\n<b>"+aste[message_id]['testo']+"</b>\n\nLike:"+likes
		try:
			bot.editMessageText(text=text, chat_id=job.context[0],message_id=job.context[1], parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup)
			bot.editMessageText(text=text, chat_id=canale,message_id=aste[message_id]['canale'], parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup_ch)
		except BadRequest:
			pass
	
def sondaggio(bot, update, args, job_queue):
	if not update.message.chat.id in id_gruppo:
		return
	if update.message.from_user.username == None:
		return
	if len(status) > 0:
		return
	name = update.message.from_user.username
	user_id = update.message.from_user.id
	date = str(datetime.datetime.now().date())+' '+ str(time.strftime('%H:%M:%S'))
	if args == list():
		update.message.reply_text("Usa /asta quantità oggetto")
		log(name, user_id, "ha usato /asta senza argomenti", date)
		return
	testo = sub('^/asta[^ ]* ', '', update.message.text)
		
	keyboard = [[InlineKeyboardButton(chr(128077), callback_data='like'), InlineKeyboardButton(chr(10060), callback_data='elimina')],
				[InlineKeyboardButton(chr(128317), callback_data='uppa'), InlineKeyboardButton("Crea asta", callback_data='crea')]]

	reply_markup = InlineKeyboardMarkup(keyboard)
	text = "Sondaggio di "+link_user(update.message.from_user.username)+" [<b>30:00</b>]\n\n<b>"+testo+"</b>\n\nLike:"
	msg = update.message.reply_text(text, parse_mode='HTML', reply_to_message_id=None, disable_web_page_preview=True, reply_markup=reply_markup)
	message_id = str(msg.message_id)
	ch_key = [[InlineKeyboardButton(chr(128077), callback_data='like'), InlineKeyboardButton('Gruppo', url=link_gruppo)]]
	reply_markup_ch = InlineKeyboardMarkup(ch_key)
	msg_ch = bot.sendMessage(canale, text, parse_mode='HTML', disable_notification=True, disable_web_page_preview=True, reply_markup=reply_markup_ch)
	aste[message_id] = dict()
	aste[message_id]['canale'] = msg_ch.message_id
	aste[message_id]['chat'] = msg.chat_id
	aste[str(msg_ch.message_id)] = message_id
	aste[message_id]['testo'] = testo
	aste[message_id]['like'] = dict()
	aste[message_id]['user'] = update.message.from_user.username
	aste[message_id]['user_id'] = update.message.from_user.id
	aste[message_id]['up'] = time.time()+60*5
	aste[message_id]['time'] = time.time()+30*60
	log(name, user_id, "ha creato un sondaggio", date)
	
	#job_queue.run_once(del_sondaggio, 30*60, context=[msg.chat.id, msg.message_id]) 
	
	job_queue.run_repeating(timer_sond, 1, context=[msg.chat.id, msg.message_id], name = 'sondaggio'+message_id)
	#update.message.reply_text(update.message.from_user.language_code)
	
	
def offri(bot, update, args):
	if not update.message.chat.id in id_gruppo:
		return
	if update.message.from_user.username == None:
		return
	global status
	name = update.message.from_user.username
	user_id = update.message.from_user.id
	date = str(datetime.datetime.now().date())+' '+ str(time.strftime('%H:%M:%S'))
	temp = time.time()
	if update.message.from_user.username == status['user']:
		update.message.reply_text('Non puoi offrire alla tua asta!')
		return
	if len(args) != 1:
		update.message.reply_text('Esempio: /offri 5')
		log(name, user_id, "ha usato /offri con argomenti sbagliati", date)
		return
	try:
		int(args[0])
	except ValueError:
		update.message.reply_text('Esempio: /offri 5')
		return
	if len(status) == 0:
		update.message.reply_text('Non ci sono aste in corso')
		log(name, user_id, "ha usato /offri senza un'asta", date)
		return
	if int(args[0]) <= status['offerta'][-1]:
		log(name, user_id, "ha offerto troppo poco", date)
		update.message.reply_text('Offerta troppo bassa!')
		return
	
	keyboard = [[InlineKeyboardButton('+1', callback_data='1'), InlineKeyboardButton("+5", callback_data='5'), InlineKeyboardButton("+10", callback_data='10')],
		[InlineKeyboardButton("Ritira", callback_data='ritira')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	status['offerta'].append(int(args[0]))
	status['offerente'].append(update.message.from_user.username)
	status['offer_time'].append(temp+10)
	status['time'].append(temp+60*2)
	status['log'].append(link_user(status['offerente'][-1])+' ha offerto '+str(status['offerta'][-1])+'$')
	testo = '- <b>'+str(status['offerta'][-1])+' monete</b>\n- <b>'+status['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>2:00</b>\n\n- '+status['log'][-1]+'\n\n'+chr(128100)+' Asta di '+link_user(status['user'])
	bot.editMessageText(text=testo, chat_id=status['chat'],message_id=status['id'], parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup)
	log(name, user_id, "ha offerto "+str(status['offerta'][-1])+" con /offri", date)
		
def timer(bot, job):
	global status
	date = str(datetime.datetime.now().date())+' '+ str(time.strftime('%H:%M:%S'))
	if status['time'][-1] <= time.time():
		job.schedule_removal()
		chiudi(bot, 'job', None)
		return
	keyboard = [[InlineKeyboardButton('+1', callback_data='1'), InlineKeyboardButton("+5", callback_data='5'), InlineKeyboardButton("+10", callback_data='10')],
		[InlineKeyboardButton("Ritira", callback_data='ritira')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	if int(search('[0-9]+:([0-9]+)', getTime(status['time'][-1])).group(1)) % 5 == 0:
		testo = '- <b>'+str(status['offerta'][-1])+' monete</b>\n- <b>'+status['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>'+getTime(status['time'][-1])+'</b>\n\n- '+status['log'][-1]+'\n\n'+chr(128100)+' Asta di '+link_user(status['user'])
		try:
			bot.editMessageText(text=testo, chat_id=status['chat'],message_id=status['id'], parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup)
		except BadRequest:
			pass
	
		
def logbut(bot, update, job_queue):
	query = update.callback_query
	if query.from_user.username == None:
		bot.answerCallbackQuery(query.id)
		return
	global aste, status
	date = str(datetime.datetime.now().date())+' '+ str(time.strftime('%H:%M:%S'))
	temp = time.time()
	
	query.message.message_id = str(query.message.message_id)
	if query.data == 'like':
		if not query.message.message_id in aste:
			bot.answerCallbackQuery(query.id)
			return
		if query.message.chat_id == canale:
			id_ch = query.message.message_id
			query.message.message_id = aste[str(id_ch)]
		else:
			id_ch = aste[str(query.message.message_id)]['canale']
		if query.from_user.username == aste[str(query.message.message_id)]['user']:
			bot.answerCallbackQuery(query.id, 'Non puoi votare al tuo sondaggio!')
			log(query.from_user.username, query.from_user.id, "ha provato a votare al suo sondaggio", date)
			return
			
		data = len(aste[str(query.message.message_id)]['like'])
		if query.from_user.username in aste[str(query.message.message_id)]['like']:
			data-=1
			aste[str(query.message.message_id)]['like'].pop(query.from_user.username)
			#text = query.message.text.replace('\n'+link_user(query.from_user.username),'')
			log(query.from_user.username, query.from_user.id, "ha tolto il like a \""+aste[str(query.message.message_id)]['testo']+"\"", date)
		else:
			data+=1
			aste[str(query.message.message_id)]['like'][query.from_user.username] = query.from_user.id
			#text=query.message.text+'\n'+link_user(query.from_user.username)
			log(query.from_user.username, query.from_user.id, "ha messo il like a \""+aste[str(query.message.message_id)]['testo']+"\"", date)
			
		if data == 3:
			ch_key = [[InlineKeyboardButton('Vai all\'asta', url=link_gruppo)]]
			reply_markup_ch = InlineKeyboardMarkup(ch_key)
			try:
				bot.sendMessage(aste[str(query.message.message_id)]['user_id'], "Il tuo sondaggio per \"<b>"+aste[str(query.message.message_id)]['testo']+"</b>\" Ã¨ arrivato a <b>3 likes</b>!", reply_markup=reply_markup_ch, parse_mode='HTML', disable_web_page_preview=True)
			except BadRequest:
				pass
		
		likes = ''
		for n in aste[str(query.message.message_id)]['like']:
			likes += '\n'+link_user(n)
			
		text = "Sondaggio di "+link_user(aste[str(query.message.message_id)]['user'])+" [<b>"+getTime(aste[str(query.message.message_id)]['time'])+"</b>]\n\n<b>"+aste[str(query.message.message_id)]['testo']+"</b>\n\nLike:"+likes
		str_data = ''
		if data != 0:
			str_data = ' '+str(data)
		keyboard = [[InlineKeyboardButton(chr(128077)+str_data, callback_data='like'), InlineKeyboardButton(chr(10060), callback_data='elimina')],
				[InlineKeyboardButton(chr(128317), callback_data='uppa'), InlineKeyboardButton("Crea asta", callback_data='crea')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		ch_key = [[InlineKeyboardButton(chr(128077)+str_data, callback_data='like'), InlineKeyboardButton('Gruppo', url=link_gruppo)]]
		reply_markup_ch = InlineKeyboardMarkup(ch_key)
		bot.editMessageText(text=text, chat_id=aste[str(query.message.message_id)]['chat'],message_id=int(query.message.message_id), parse_mode='HTML',disable_web_page_preview=True, reply_markup=reply_markup)
		bot.editMessageText(text=text, chat_id=canale, message_id=id_ch, parse_mode='HTML',disable_web_page_preview=True, reply_markup=reply_markup_ch)
		bot.answerCallbackQuery(query.id)
	elif query.data == 'crea':
		id_asta = str(query.message.message_id)
		if query.from_user.username != aste[id_asta]['user'] and query.from_user.id not in id_admin:
			bot.answerCallbackQuery(query.id, 'Non Ã¨ un tuo sondaggio!')
			return
		if len(aste[id_asta]['like']) < 3 and query.from_user.id not in id_admin:
			bot.answerCallbackQuery(query.id, "Minimo 3 likes!")
			return
		if len(status) > 0:
			bot.answerCallbackQuery(query.id, "C'Ã¨ giÃ  un'asta!")
			return
		keyboard = [[InlineKeyboardButton('SÃ¬', callback_data='si_'+str(query.message.message_id)), InlineKeyboardButton("No", callback_data='no_'+str(query.message.message_id))]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		bot.sendMessage(query.message.chat_id, "@"+query.from_user.username+", vuoi creare l'asta?", parse_mode='HTML', reply_markup=reply_markup)
		bot.answerCallbackQuery(query.id)
		log(query.from_user.username, query.from_user.id, "ha premuto il pulsante crea di \""+aste[id_asta]['testo']+"\"", date)
	elif search("^si_", query.data):
		id_asta = sub("^si_", "", query.data)
		if query.from_user.username != aste[id_asta]['user'] and query.from_user.id not in id_admin:
			bot.answerCallbackQuery(query.id, "Non Ã¨ la tua asta!")
			return
		if len(aste[id_asta]['like']) < 3 and query.from_user.id not in id_admin:
			bot.deleteMessage(query.message.chat_id, query.message.message_id)
			bot.answerCallbackQuery(query.id, "Minimo 3 likes!")
			return
		if len(status) > 0:
			bot.answerCallbackQuery(query.id, "C'Ã¨ giÃ  un'asta!")
			return
		likes = ''
		str_likes = ''
		for n in aste[id_asta]['like']:
			likes += '\n@'+n
			str_likes += '@'+n+' '
			try:
				keyboard = [[InlineKeyboardButton('Partecipa!', url=link_gruppo)]]
				reply = InlineKeyboardMarkup(keyboard)
				bot.sendMessage(aste[id_asta]['like'][n], 'L\'asta per "<b>'+aste[id_asta]['testo']+'</b>" Ã¨ partita!', parse_mode='HTML', reply_markup=reply)
			except:
				pass
		str_likes += '\nAsta partita!'
		#base = 'Asta di '+link_user(aste[id_asta]['user'])+"\n\n<b>"+aste[id_asta]['testo']+"</b>\n\nLike:" #Offerente: -\nOfferta attuale: -\nScadenza: 5 minuti"
		#bot.editMessageText(text=base+likes+'\n\n<i>Asta creata!</i>', chat_id=query.message.chat_id,message_id=int(id_asta), parse_mode='HTML', disable_web_page_preview=True)
		bot.deleteMessage(query.message.chat_id, int(id_asta))
		bot.deleteMessage(canale, aste[id_asta]['canale'])
		bot.deleteMessage(query.message.chat_id, query.message.message_id)
		for j in job_queue.jobs():
			try:
				if j.context[1] == int(id_asta):
					j.schedule_removal()
			except:
				pass
		
		
		tag_msg = bot.sendMessage(query.message.chat_id, str_likes)
		
		keyboard = [[InlineKeyboardButton('+1', callback_data='1'), InlineKeyboardButton("+5", callback_data='5'), InlineKeyboardButton("+10", callback_data='10')],
		[InlineKeyboardButton("Ritira", callback_data='ritira')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		testo = '- <b>0 monete</b>\n- <b>'+aste[id_asta]['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>2:00</b>\n\n- '+link_user(aste[id_asta]['user'])+' ha creato l\'asta\n\n'+chr(128100)+' Asta di '+link_user(aste[id_asta]['user'])
		msg = bot.sendMessage(query.message.chat_id, testo, disable_web_page_preview=True, parse_mode='HTML', reply_markup=reply_markup)
		if msg.chat.type == 'supergroup':
			bot.pinChatMessage(query.message.chat_id, msg.message_id, disable_notification=True)
		bot.answerCallbackQuery(query.id, "Asta creata!")
		keyboard = [[InlineKeyboardButton('Vai all\'asta!', url=link_gruppo)]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		msg_ch = bot.sendMessage(canale, "<b>Asta in corso:</b>\n\n"+aste[id_asta]['testo']+"\n\n"+chr(128100)+' Asta di '+link_user(aste[id_asta]['user']), disable_web_page_preview=True, parse_mode='HTML', reply_markup=reply_markup)
		bot.sendMessage(175104816, 'asta creata')
		status['canale'] = msg_ch.message_id
		status['tag_msg'] = tag_msg.message_id
		status['testo'] = aste[id_asta]['testo']
		status['user'] = aste[id_asta]['user']
		status['id'] = msg.message_id
		status['chat'] = query.message.chat_id
		status['time'] = [temp+60*2]
		status['offer_time'] = [temp+10]
		status['offerente'] = ['-']
		status['offerta'] = [0]
		status['ritiro'] = dict()
		status['log'] = [ link_user(status['user'])+' ha creato l\'asta' ]
		
		
		log(query.from_user.username, query.from_user.id, 'ha creato l\'asta "'+aste[id_asta]['testo']+'"', date)
		aste.pop(str(aste[id_asta]['canale']))
		aste.pop(id_asta)
		
		#j = JobQueue(bot)
		job_queue.run_repeating(timer, 1, name = 'asta')
		#j.start()
		
	elif search("^no_", query.data):
		id_asta = sub("^no_", "", query.data)
		if query.from_user.username != aste[id_asta]['user']:
			bot.answerCallbackQuery(query.id, "Non Ã¨ la tua asta!")
			return
		bot.deleteMessage(query.message.chat_id, query.message.message_id)
		bot.answerCallbackQuery(query.id, 'Messaggio eliminato')
		log(query.from_user.username, query.from_user.id, 'ha eliminato il messaggio di conferma', date)
		
	elif query.data == '1' or query.data == '5' or query.data == '10' or query.data == 'ritira':
		if len(status) == 0:
			bot.answerCallbackQuery(query.id, "Asta finita!")
			return
		if query.from_user.username == status['user']:
			bot.answerCallbackQuery(query.id, "Non puoi offrire alla tua asta!")
			log(query.from_user.username, query.from_user.id, 'ha provato ad offrire a una sua asta', date)
			return
		keyboard = [[InlineKeyboardButton('+1', callback_data='1'), InlineKeyboardButton("+5", callback_data='5'), InlineKeyboardButton("+10", callback_data='10')],
		[InlineKeyboardButton("Ritira", callback_data='ritira')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		if query.data == 'ritira':
			if query.from_user.username == status['offerente'][-1]:
				if status['offer_time'][-1] >= temp:
					if query.from_user.username in status['ritiro'] and status['ritiro'][query.from_user.username] >= 2:
						bot.answerCallbackQuery(query.id, 'Hai ritirato troppe volte!')
						return
					money = status['offerta'][-1]
					if query.from_user.username not in status['ritiro']:
						status['ritiro'][query.from_user.username] = 1
					else:
						status['ritiro'][query.from_user.username] += 1
					
					status['log'].append(link_user(status['offerente'][-1])+' ha ritirato l\'offerta, attuale offerta di: '+link_user(status['offerente'][-2]))
					status['offerta'].remove(status['offerta'][-1])
					status['offerente'].remove(status['offerente'][-1])
					status['offer_time'].remove(status['offer_time'][-1])
					status['time'].remove(status['time'][-1])
					if status['offerta'][-1] == 1:
						testo = '- <b>'+str(status['offerta'][-1])+' moneta</b>\n- <b>'+status['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>'+getTime(status['time'][-1])+'</b>\n\n- '+status['log'][-1]+'\n\n'+chr(128100)+' Asta di '+link_user(status['user'])
					else:
						testo = '- <b>'+str(status['offerta'][-1])+' monete</b>\n- <b>'+status['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>'+getTime(status['time'][-1])+'</b>\n\n- '+status['log'][-1]+'\n\n'+chr(128100)+' Asta di '+link_user(status['user'])
					bot.editMessageText(text=testo, chat_id=status['chat'],message_id=status['id'], parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup)
					bot.answerCallbackQuery(query.id, 'Hai ritirato la tua offerta!')
					log(query.from_user.username, query.from_user.id, 'ha ritirato l\'offerta di '+str(money)+'$ dall\'asta "'+status['testo']+'"', date)
				else:
					bot.answerCallbackQuery(query.id, 'Tempo scaduto, non puoi ritirare!')
					log(query.from_user.username, query.from_user.id, 'non ha potuto ritirare l\'offerta, tempo scaduto. Asta: "'+status['testo']+'"', date)
			else:
				bot.answerCallbackQuery(query.id, "L'ultima offerta non Ã¨ tua!")
				log(query.from_user.username, query.from_user.id, 'non ha potuto ritirare l\'offerta, ultima offerta non sua. Asta: "'+status['testo']+'"', date)
			return
		status['offerta'].append(status['offerta'][-1]+int(query.data))
		status['offerente'].append(query.from_user.username)
		status['offer_time'].append(temp+10)
		status['time'].append(temp+60*2)
		status['log'].append(link_user(status['offerente'][-1])+' ha offerto '+str(status['offerta'][-1])+'$')
		
		if status['offerta'][-1] == 1:
			testo = '- <b>'+str(status['offerta'][-1])+' moneta</b>\n- <b>'+status['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>2:00</b>\n\n- '+status['log'][-1]+'\n\n'+chr(128100)+' Asta di '+link_user(status['user'])
		else:
			testo = '- <b>'+str(status['offerta'][-1])+' monete</b>\n- <b>'+status['testo']+'</b>\n\n'+chr(9201)+' Scadenza <b>2:00</b>\n\n- '+status['log'][-1]+'\n\n'+chr(128100)+' Asta di '+link_user(status['user'])
		
		bot.editMessageText(text=testo, chat_id=status['chat'],message_id=status['id'], parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup)
		bot.answerCallbackQuery(query.id, 'Hai offerto '+str(status['offerta'][-1])+'$')
		log(query.from_user.username, query.from_user.id, 'ha offerto '+str(status['offerta'][-1])+'$. Asta: "'+status['testo']+'"', date)
	
	elif query.data == 'uppa':
		message_id = str(query.message.message_id)
		if len(status) > 0:
			bot.answerCallbackQuery(query.id, "Non puoi uppare durante un'asta!")
			return
		if query.from_user.username != aste[message_id]['user'] and query.from_user.id not in id_admin:
			bot.answerCallbackQuery(query.id, "Non Ã¨ un tuo sondaggio!")
			return
		if aste[message_id]['up'] >= time.time() and query.from_user.id not in id_admin:
			bot.answerCallbackQuery(query.id, "Puoi uppare ogni 5 minuti!")
			return
		
		
		likes = ''
		for n in aste[message_id]['like']:
			likes += '\n'+link_user(n)
			
		n_like = len(aste[message_id]['like'])
		if n_like == 0:
			n_like = ''
		else:
			n_like = ' '+str(n_like)
		
		bot.deleteMessage(query.message.chat_id, query.message.message_id)
		keyboard = [[InlineKeyboardButton(chr(128077)+n_like, callback_data='like'), InlineKeyboardButton(chr(10060), callback_data='elimina')],
				[InlineKeyboardButton(chr(128317), callback_data='uppa'), InlineKeyboardButton("Crea asta", callback_data='crea')]]

		reply_markup = InlineKeyboardMarkup(keyboard)
		
		text = "Sondaggio di "+link_user(aste[message_id]['user'])+" [<b>"+getTime(aste[message_id]['time'])+"</b>]\n\n<b>"+aste[message_id]['testo']+"</b>\n\nLike:"+likes
		msg = bot.sendMessage(query.message.chat_id, text, parse_mode='HTML', disable_web_page_preview=True, reply_markup=reply_markup)
		new_id = str(msg.message_id)
		aste[new_id] = aste.pop(message_id)
		aste[str(aste[new_id]['canale'])] = msg.message_id
		aste[new_id]['up'] = time.time()+60*5
		
		for j in job_queue.jobs():
			try:
				if j.context[1] == int(message_id):
					j.schedule_removal()
			except:
				pass
	
		#job_queue.run_once(del_sondaggio, 30*60, context=[msg.chat.id, msg.message_id])
		job_queue.run_repeating(timer_sond, 1, context=[msg.chat.id, msg.message_id], name = 'sondaggio'+str(msg.message_id))
		
	
	elif query.data == 'elimina':
		for j in job_queue.jobs():
			try:
				if int(j.context[1]) == int(query.message.message_id):
					j.schedule_removal()
			except:
				pass
		if query.from_user.username != aste[str(query.message.message_id)]['user'] and query.from_user.id not in id_admin:
			bot.answerCallbackQuery(query.id, "Non Ã¨ un tuo sondaggio!")
			return
		bot.deleteMessage(canale, aste[str(query.message.message_id)]['canale'])
		aste.pop(str(aste[str(query.message.message_id)]['canale']))
		aste.pop(str(query.message.message_id))
		
		
			
		bot.deleteMessage(query.message.chat_id, query.message.message_id)
		
		
def inlinequery(bot, update):
	global status, aste
	query = update.inline_query.query
	results = list()
	user_id = update.inline_query.from_user.id
	
	if len(status) > 0:
		keyboard = [[InlineKeyboardButton('Partecipa!', url=link_gruppo)]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		results.append(InlineQueryResultArticle(id=uuid4(),
											title="Asta",
											description=status['testo'],
											reply_markup=reply_markup,
											input_message_content=InputTextMessageContent(
												"Asta in corso nel <b>Salone Aste</b>!\n\n"+status['testo'], disable_web_page_preview=True, parse_mode='HTML'
											)))
	
	for id_asta in aste:
		try:
			if aste[str(id_asta)]['testo']:
				nome = aste[str(id_asta)]['testo']
				keyboard = [[InlineKeyboardButton('Vota l\'asta!', url=url_ch+str(aste[str(id_asta)]['canale']))]]
				reply_markup = InlineKeyboardMarkup(keyboard)
				results.append(InlineQueryResultArticle(id=uuid4(),
												title="Sondaggio",
												description=nome,
												reply_markup=reply_markup,
												input_message_content=InputTextMessageContent(
													"Sondaggio nel <b>Salone Aste</b>!\n\n"+nome, disable_web_page_preview=True, parse_mode='HTML'
												)))
		except TypeError:
			pass
		except KeyError:
			pass
											
	if results == list():
		keyboard = [[InlineKeyboardButton('Entra nel gruppo!', url=link_gruppo)]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		results.append(InlineQueryResultArticle(id=uuid4(),
											title="Non ho trovato nulla...",
											description="Non ci sono aste",
											reply_markup=reply_markup,
											input_message_content=InputTextMessageContent(
												"<b>Entra nel Salone Aste</b>, metti all'asta i tuoi oggetti :)", disable_web_page_preview=True, parse_mode='HTML'
											)))
											
	update.inline_query.answer(results,cache_time=0)

def pinned(bot, update):
	if update.message.chat_id in id_gruppo:
		bot.deleteMessage(update.message.chat_id, update.message.message_id)
	
def log_request(bot, update):
	if update.message.from_user.id in id_admin:
		f = open("log.txt", "rb")
		bot.sendDocument(update.message.from_user.id, f)
		
def pin(bot, update):
	if update.message.from_user.id in id_admin:
		f = open("pin.txt", "w")
		f.write(str(update.message.reply_to_message.message_id))
		f.close()
		update.message.reply_text('Messaggio salvato.')
		
def delete(bot, update):
	if update.message.from_user.id in id_admin and len(args) == 1:
		f = open("msgs.txt", "w")
		f.write(str(update.message.reply_to_message.message_id))
		f.close()
		update.message.reply_text('Messaggio salvato.')
		
def loschi(bot, update):
	if update.message.from_user.id == 187465921:
		bot.send_message(chat_id=update.message.chat_id,text = "A rapporto!")

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
	updater = Updater("bot_api_key")

    # Get the dispatcher to register handlers
	dp = updater.dispatcher

    # on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	#dp.add_handler(CommandHandler("cerca", cerca, pass_args=True))
	dp.add_handler(CommandHandler("asta", sondaggio, pass_args=True, pass_job_queue=True))
	dp.add_handler(CommandHandler("offri", offri, pass_args=True))
	dp.add_handler(InlineQueryHandler(inlinequery))
	dp.add_handler(CallbackQueryHandler(logbut, pass_job_queue=True))
	dp.add_handler(CommandHandler("log", log_request))
	dp.add_handler(CommandHandler("pin", pin))
	dp.add_handler(CommandHandler("chiudi", chiudi, pass_job_queue=True))
	dp.add_handler(MessageHandler(Filters.status_update.pinned_message, pinned))
	#dp.add_handler(CommandHandler('loschi',loschi))
	#dp.add_handler(CommandHandler('test',test))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.all, echo))

    # log all errors
	dp.add_error_handler(error)

    # Start the Bot
	updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
    main()
