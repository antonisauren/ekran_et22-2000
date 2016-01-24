#encoding: UTF-8

from PIL import ImageDraw, ImageFont, Image

class et22_2000_renderer(abstractscreenrenderer):
	def __init__(self, lookup_path, name, cab):
		# wczytanie obrazka
		self.moj_obrazek = Image.open(lookup_path + "pulpit.png")
		# wczytanie czcionki
		self.font = ImageFont.truetype(lookup_path + "MyriadPro-Regular.otf", 22)		
		self.maly_font = ImageFont.truetype(lookup_path + "MyriadPro-Regular.otf", 16)	
		self.bardzo_maly_font = ImageFont.truetype(lookup_path + "MyriadPro-Regular.otf", 12)	
		self.duzy_font = ImageFont.truetype(lookup_path + "MyriadPro-Regular.otf", 35)
		# rysujemy stale pojawiajace sie elementy zeby ich pozniej nie powtarzac bez sensu
		draw = ImageDraw.Draw(self.moj_obrazek)
		draw.rectangle((240,470,400,510), fill=(255,255,255)) # tlo slupkow predkosci aktualnej i zadanej
		draw.rectangle((560,180,630,360), fill=(255,255,255)) # tlo slupka padu
		draw.rectangle((660,180,730,360), fill=(255,255,255)) # tlo slupka napiecia
		draw.rectangle((270,410,380,440), fill=(255,255,255)) # tlo (ramka) boxow NJ/NB
		draw.rectangle((500,410,845,540), fill=(255,255,255)) # tlo info boxa
		draw.rectangle((502,412,829,538), fill=(40,43,44)) # tlo (ramka) info boxa
		draw.rectangle((830,412,845,538), fill=(0,100,255)) # niebieski pasek z boku info boxa
		draw.rectangle((272,412,324,438), fill=(40,43,44)) # tlo boxu NJ
		draw.text((276, 420), 'NJ', font=self.maly_font, fill=(255,255,255))
		draw.rectangle((326,412,378,438), fill=(40,43,44)) # tlo boxu NB
		draw.text((330, 420), 'NB', font=self.maly_font, fill=(255,255,255))

		draw.text((300, 383), 'km/h', font=self.font, fill=(255,255,255)) # pod wskazowka
		draw.text((175, 445), 'Predkosc:', font=self.font, fill=(255,255,255))
		draw.text((175, 473), 'Aktualna', font=self.maly_font, fill=(255,255,255))
		draw.text((185, 494), 'Zadana', font=self.maly_font, fill=(255,255,255))
		draw.text((440, 473), 'km/h', font=self.maly_font, fill=(255,255,255)) # za aktualna
		draw.text((440, 494), 'km/h', font=self.maly_font, fill=(255,255,255)) # za zadana

		draw.text((174,112), name.upper(), font=self.font, fill=(255,255,255))
		draw.text((464,105), 'JAZDA', font=self.duzy_font, fill=(255,255,255))
		if cab==1:
			draw.text((754,112), 'Kabina A', font=self.font, fill=(255,255,255))
		if cab==-1:
			draw.text((754,112), 'Kabina B', font=self.font, fill=(255,255,255))


		# skala predkosci
		draw.text((237, 525), '0', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((257, 525), '20', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((277, 525), '40', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((298, 525), '60', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((318, 525), '80', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((336, 525), '100', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((356, 525), '120', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((376, 525), '140', font=self.bardzo_maly_font, fill=(255,255,255))
		# skala predkosci pionowe kreseczki
		draw.line([(240,510),(240,520)],fill=(255,255,255),width=1)
		draw.line([(263,510),(263,520)],fill=(255,255,255),width=1)
		draw.line([(283,510),(283,520)],fill=(255,255,255),width=1)
		draw.line([(304,510),(304,520)],fill=(255,255,255),width=1)
		draw.line([(324,510),(324,520)],fill=(255,255,255),width=1)
		draw.line([(345,510),(345,520)],fill=(255,255,255),width=1)
		draw.line([(365,510),(365,520)],fill=(255,255,255),width=1)
		draw.line([(386,510),(386,520)],fill=(255,255,255),width=1)

		draw.text((778, 210), 'kierunek', font=self.bardzo_maly_font, fill=(255,255,255))
		draw.text((592, 165), 'A', font=self.maly_font, fill=(255,255,255))
		draw.text((690, 165), 'kV', font=self.maly_font, fill=(255,255,255))

		# skala poziome kreseczki dla pradu
		draw.line([(550,181),(560,181)],fill=(255,255,255),width=1)
		draw.line([(550,202),(560,202)],fill=(255,255,255),width=1)
		draw.line([(550,225),(560,225)],fill=(255,255,255),width=1)
		draw.line([(550,247),(560,247)],fill=(255,255,255),width=1)
		draw.line([(550,270),(560,270)],fill=(255,255,255),width=1)
		draw.line([(550,292),(560,292)],fill=(255,255,255),width=1)
		draw.line([(550,315),(560,315)],fill=(255,255,255),width=1)
		draw.line([(550,337),(560,337)],fill=(255,255,255),width=1)
		draw.line([(550,360),(560,360)],fill=(255,255,255),width=1)

		draw.text((523,174), '800', font=self.maly_font, fill=(255,255,255))
		draw.text((523,195), '700', font=self.maly_font, fill=(255,255,255))
		draw.text((523,217), '600', font=self.maly_font, fill=(255,255,255))
		draw.text((523,240), '500', font=self.maly_font, fill=(255,255,255))
		draw.text((523,263), '400', font=self.maly_font, fill=(255,255,255))
		draw.text((523,285), '300', font=self.maly_font, fill=(255,255,255))
		draw.text((523,308), '200', font=self.maly_font, fill=(255,255,255))
		draw.text((523,330), '100', font=self.maly_font, fill=(255,255,255))
		draw.text((540,353), '0', font=self.maly_font, fill=(255,255,255))

		# skala poziome kreseczki dla napiecia
		draw.line([(730,181),(740,181)],fill=(255,255,255),width=1)
		draw.line([(730,225),(740,225)],fill=(255,255,255),width=1)
		draw.line([(730,270),(740,270)],fill=(255,255,255),width=1)
		draw.line([(730,315),(740,315)],fill=(255,255,255),width=1)
		draw.line([(730,360),(740,360)],fill=(255,255,255),width=1)

		draw.text((745,174), '4', font=self.maly_font, fill=(255,255,255))
		draw.text((745,217), '3', font=self.maly_font, fill=(255,255,255))
		draw.text((745,263), '2', font=self.maly_font, fill=(255,255,255))
		draw.text((745,308), '1', font=self.maly_font, fill=(255,255,255))
		draw.text((745,353), '0', font=self.maly_font, fill=(255,255,255))

		draw.polygon([(790,200),(790,190), (780,190), (800, 160), (820, 190), (810, 190), (810,200)],fill=(255,255,255)) # tlo strzalki kierunkowej naprzod
		draw.polygon([(790,230),(790,240), (780,240), (800, 270), (820, 240), (810, 240), (810,230)],fill=(255,255,255)) # tlo strzalki kierunkowej wtyl

		# rysujemy kolko na srodku igly
		draw.pieslice((315,300,345,330), 0, 360, fill=(166,118,253))
	def _render(self, state):
		speed = float(state['velocity'])
		zadana = state['velocity_desired']
		# kopia obrazka na potrzeby tego jednego renderowania
		obrazek = self.moj_obrazek.copy()
		# chcemy rysowac po teksturze pulpitu
		draw = ImageDraw.Draw(obrazek)

		# dlugosc slupka predkosci i rysowanie
		slide = speed * 156 / 150 + 242
		draw.rectangle((242,472,slide,489), fill=(156,108,243))
		draw.rectangle((slide,472,398,489), fill=(40,43,44))
		# dlugosc slulpka zadanej
		slide = zadana * 156 / 150 + 242
		draw.rectangle((242,492,slide,508), fill=(0,150,0))
		draw.rectangle((slide,492,398,508), fill=(40,43,44))
		# predkosc dla slupkow
		self.print_fixed_with(draw, '%d' % speed, (410, 473), 3, self.maly_font, (255,255,255))
		self.print_fixed_with(draw, '%d' % zadana, (410, 494), 3, self.maly_font, (255,255,255))
		# liczymy pozycje igly
		rotate = speed * 240 / 150 - 120
		rad =  radians(rotate)
		point = (0,-100)
		rotated_point = (point[0]*cos(rad)-point[1]*sin(rad) + 330,point[0]*sin(rad)+point[1]*cos(rad) + 315)
		point = (3,0)
		rotated_base_one = (point[0]*cos(rad)-point[1]*sin(rad) + 330,point[0]*sin(rad)+point[1]*cos(rad) + 315)
		point = (-3,0)
		rotated_base_two = (point[0]*cos(rad)-point[1]*sin(rad) + 330,point[0]*sin(rad)+point[1]*cos(rad) + 315)
		# rysujemy igle
		draw.polygon([rotated_base_one,rotated_point,rotated_base_two],fill=(166,118,253))
		# liczymy pozycje trojkacika predkosci zadanej
		rotate = zadana * 240 / 150 - 120
		rad =  radians(rotate)
		point = (0,-137)
		rotated_point = (point[0]*cos(rad)-point[1]*sin(rad) + 330,point[0]*sin(rad)+point[1]*cos(rad) + 315)
		point = (9,-155)
		rotated_base_one = (point[0]*cos(rad)-point[1]*sin(rad) + 330,point[0]*sin(rad)+point[1]*cos(rad) + 315)
		point = (-9,-155)
		rotated_base_two = (point[0]*cos(rad)-point[1]*sin(rad) + 330,point[0]*sin(rad)+point[1]*cos(rad) + 315)
		# rysujemy strzalke
		draw.polygon([rotated_base_one,rotated_point,rotated_base_two],fill=(0,255,0))
		#self.rotate_and_paste(obrazek, self.igielka, rotate, (330,320), (0, 50))

		# zaznaczamy kierunek jazdy		
		if state['direction'] == 1:
			kolor = (0,255,0)
		else:
			kolor = (40,43,44)
		draw.polygon([(792,198),(792,188), (784,188), (800, 163), (816, 188), (808, 188), (808,198)],fill=kolor) # strzalka kierunkowa naprzod

		if state['direction'] == -1:
			kolor = (0,255,0)
		else:
			kolor = (40,43,44)
		draw.polygon([(792,232),(792,242), (784,242), (800, 267), (816, 242), (808, 242), (808,232)],fill=kolor) # strzalka kierunkowa wtyl

		# slupek pradu i jego wartosc
		kolor = (100,255,100)
		prad = state['im']
		if prad < 0:
			prad = 0
			kolor = (255,255,255)
		pos = 358 - (prad * 174 / 800)
		draw.rectangle((562,pos,628,358), fill=(150,255,150))
		draw.rectangle((562,182,628,pos), fill=(40,43,44))
		self.print_fixed_with(draw, '%dA' % prad, (580, 365), 4, self.font, kolor)

		# slupek napiecia i jego wartosc
		kolor = (100,255,100)
		prad = state['voltage']
		if prad < 0:
			prad = 0
			kolor = (255,255,255)
		pos = 358 - (prad * 174 / 4000)
		draw.rectangle((662,pos,728,358), fill=(150,255,150))
		draw.rectangle((662,182,728,pos), fill=(40,43,44))
		self.print_fixed_with(draw, '%dV' % prad, (670, 365), 5, self.font, kolor)

		# duzy tekst z predkoscia w pod wskazowka
		v = '%.1f' % speed
		self.print_fixed_with(draw, v[:-2], (285, 355), 3, self.duzy_font, (255,255,255)) # zapis v[:-2] oznacza wszystko oprocz dwoch ostatnich znakow (zapis od:do)
		draw.text((340, 365), v[-2:], font=self.font, fill=(255,255,255)) # zapis [-2:] oznacza wsystko od drugiego od konca znaku (zapis od:do)

		# jakie jest nastawienie jazdy i bocznikowania
		nj = state['main_ctrl_actual_pos']-3
		if nj<0:
			nj = 0
		nb = 0
		kolor = (255,50,50)
		if nj%10 == 0:
			kolor = (255,255,255)
			nb = nj/10
		self.print_fixed_with(draw, '%d' % nj, (277, 416), 4, self.font, kolor)
		if nb == 0:
			kolor = (255,255,255)
		else:
			kolor = (10,155,10)
		self.print_fixed_with(draw, '%d' % nb, (332, 416), 4, self.font, kolor)	

		# wyswietlamy wiadomosci tekstowe
		msg_x_start = 502
		msg_y_start = 412
		msg_x_end = 829

		if state['converter']:
			msg = 'Smarowanie zalaczone'
			rozmiar = self.maly_font.getsize(msg)
			draw.rectangle((msg_x_start, msg_y_start, msg_x_end, msg_y_start + rozmiar[1]), fill=(60,60,60))
			draw.text((msg_x_start+10,msg_y_start+2), msg, fill=(255,255,255), font=self.maly_font)
			msg_y_start += rozmiar[1]

		if state['compress']:
			msg = 'Praca sprezaki'
			rozmiar = self.maly_font.getsize(msg)
			draw.rectangle((msg_x_start, msg_y_start, msg_x_end, msg_y_start + rozmiar[1]), fill=(50,50,50))
			draw.text((msg_x_start+10,msg_y_start+2), msg, fill=(255,155,155), font=self.maly_font)
			msg_y_start += rozmiar[1]

		if state['slipping_wheels']:
			msg = 'POSLIZG!'
			rozmiar = self.maly_font.getsize(msg)
			draw.rectangle((msg_x_start, msg_y_start, msg_x_end, msg_y_start + rozmiar[1]), fill=(255,0,0))
			draw.text((msg_x_start+10,msg_y_start+2), msg, fill=(255,255,255), font=self.maly_font)
			msg_y_start += rozmiar[1]	


		if state['converter_overload']:
			msg = 'Zadzialal przekaznik nadmiarowy przetwornicy'
			rozmiar = self.maly_font.getsize(msg)
			draw.rectangle((msg_x_start, msg_y_start, msg_x_end, msg_y_start + rozmiar[1]), fill=(50,50,50))
			draw.text((msg_x_start+10,msg_y_start+2), msg, fill=(255,50,50), font=self.maly_font)
			msg_y_start += rozmiar[1]	


		if state['fuse']:
			msg = 'Zadzialal przekaznik nadmiarowy'
			rozmiar = self.maly_font.getsize(msg)
			draw.rectangle((msg_x_start, msg_y_start, msg_x_end, msg_y_start + rozmiar[1]), fill=(50,50,50))
			draw.text((msg_x_start+10,msg_y_start+2), msg, fill=(255,55,55), font=self.maly_font)
			msg_y_start += rozmiar[1]	

		newImage = Image.new('RGB', (1024, 1024))
		newImage.paste(obrazek, (0,1024-obrazek.size[1],1024,1024))
		return newImage


