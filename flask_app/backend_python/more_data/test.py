from bs4 import BeautifulSoup

html = '''

	<div class="playlog_top_container p_r">
		<img src="https://maimaidx-eng.com/maimai-mobile/img/diff_master.png" class="playlog_diff v_b">
						<div class="sub_title t_c f_r f_11">
			<span class="red f_b v_b">TRACK 04</span>　<span class="v_b">2023/04/27 13:58</span>
		</div>
		<div class="clearfix"></div>
	</div>
	<div class="playlog_master_container">
		<div class="basic_block m_5 p_5 p_l_10 f_13 break"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/clear.png" class="w_80 f_r">Heavenly Blast</div>
		<div class="p_r f_0">
			<img loading="lazy" src="https://maimaidx-eng.com/maimai-mobile/img/Music/b93bb5411292f1d8.png" class="music_img m_5 m_r_0 f_l">
										<img src="https://maimaidx-eng.com/maimai-mobile/img/music_dx.png" class="playlog_music_kind_icon">
						<div class="playlog_result_block m_t_5 f_l">
				<div class="playlog_achievement_label_block">
					<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/achievement.png">
				</div>
									<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/newrecord.png" class="playlog_achievement_newrecord">
								<div class="playlog_achievement_txt t_r">95<span class="f_20">.8029%</span></div>
				<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/aaa.png?ver=1.30" class="playlog_scorerank">
									<img src="https://maimaidx-eng.com/maimai-mobile/img/line_02.png" class="playlog_scoreline f_r">
				<div class="playlog_result_innerblock basic_block p_5 f_13">
					<div class="playlog_score_block f_0">
						<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/deluxscore.png" class="w_80">
												<div class="white p_r_5 f_15 f_r">2,744 / 3,507</div>
											</div>
					<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/fc_dummy.png?ver=1.30" class="h_35 m_5 f_l">
										<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/fs_dummy.png?ver=1.30" class="h_35 m_5 f_l">
																<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/1st.png" class="playlog_matching_icon f_r">
																	<div class="clearfix"></div>
				</div>
				<div class="clearfix"></div>
							</div>
		</div>
		<div class="clearfix"></div>
	</div>


	<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/character.png" class="m_t_5 f_l">
	<div class="clearfix"></div>
						<div class="playlog_chara_container">
				<div class="playlog_chara_block">
					<div class="chara_cycle_trim">
						<img loading="lazy" src="https://maimaidx-eng.com/maimai-mobile/img/Chara/fc3e11702dd328b2.png" class="chara_cycle_img">					</div>
				</div>
				<div class="playlog_chara_star_block f_12"><img src="https://maimaidx-eng.com/maimai-mobile/img/icon_star.png" class="v_b">×5</div>
				<div class="playlog_chara_lv_block f_13">Lv1319</div>
			</div>
								<div class="playlog_chara_container">
				<div class="playlog_chara_block">
					<div class="chara_cycle_trim">
						<img loading="lazy" src="https://maimaidx-eng.com/maimai-mobile/img/Chara/794ae289c763d272.png" class="chara_cycle_img">					</div>
				</div>
				<div class="playlog_chara_star_block f_12"><img src="https://maimaidx-eng.com/maimai-mobile/img/icon_star.png" class="v_b">×5</div>
				<div class="playlog_chara_lv_block f_13">Lv2859</div>
			</div>
								<div class="playlog_chara_container">
				<div class="playlog_chara_block">
					<div class="chara_cycle_trim">
						<img loading="lazy" src="https://maimaidx-eng.com/maimai-mobile/img/Chara/a2cf9c66d5ecabe3.png" class="chara_cycle_img">					</div>
				</div>
				<div class="playlog_chara_star_block f_12"><img src="https://maimaidx-eng.com/maimai-mobile/img/icon_star.png" class="v_b">×5</div>
				<div class="playlog_chara_lv_block f_13">Lv2683</div>
			</div>
								<div class="playlog_chara_container">
				<div class="playlog_chara_block">
					<div class="chara_cycle_trim">
						<img loading="lazy" src="https://maimaidx-eng.com/maimai-mobile/img/Chara/8dfe037b9d242f5d.png" class="chara_cycle_img">					</div>
				</div>
				<div class="playlog_chara_star_block f_12"><img src="https://maimaidx-eng.com/maimai-mobile/img/icon_star.png" class="v_b">×4</div>
				<div class="playlog_chara_lv_block f_13">Lv587</div>
			</div>
								<div class="playlog_chara_container">
				<div class="playlog_chara_block">
					<div class="chara_cycle_trim">
						<img loading="lazy" src="https://maimaidx-eng.com/maimai-mobile/img/Chara/c8acded545a92d37.png" class="chara_cycle_img">					</div>
				</div>
				<div class="playlog_chara_star_block f_12"><img src="https://maimaidx-eng.com/maimai-mobile/img/icon_star.png" class="v_b">×3</div>
				<div class="playlog_chara_lv_block f_13">Lv167</div>
			</div>
				<img src="https://maimaidx-eng.com/maimai-mobile/img/line_01.png" class="w_450 m_b_5">
	<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/detail.png" class="f_l">
			<div class="playlog_fl_block m_b_5 f_r f_12">
			<div class="w_96 f_l t_r"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/fast.png" class="h_10 m_3 m_l_10 f_l"><div class="p_t_5">351</div></div>
			<div class="w_96 f_l t_r"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/late.png" class="h_10 m_3 m_l_10 f_l"><div class="p_t_5">169</div></div>
		</div>
		<div class="clearfix"></div>
	<div class="p_5">
		<table class="playlog_notes_detail t_r f_l f_11 f_b" style="width: 100%;">
			<tbody><tr>
				<th></th>
				<td class="t_c f_0"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/criticalperfect.png"></td>
				<td class="t_c f_0"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/perfect.png"></td>
				<td class="t_c f_0"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/great.png"></td>
				<td class="t_c f_0"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/good.png"></td>
				<td class="t_c f_0"><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/miss.png"></td>
			</tr>
			<tr>
				<th class=""><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/tap.png"><br>-<span title="3.2002%">3.20%</span> (<span title="52.3782%">52.38%</span>)</th>
									<td>422</td>
					<td>330</td>
					<td>95<br>(<span title="-1.1157%">-1.12%</span>)</td>
					<td>19<br>(<span title="-0.5578%">-0.56%</span>)</td>
					<td>26<br>(<span title="-1.5267%">-1.53%</span>)</td>
							</tr>
			<tr>
				<th class=""><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/hold.png"><br>-<span title="0.6224%">0.62%</span> (<span title="9.8649%">9.86%</span>)</th>
									<td>47</td>
					<td>26</td>
					<td>4<br>(<span title="-0.0940%">-0.09%</span>)</td>
					<td>5<br>(<span title="-0.2936%">-0.29%</span>)</td>
					<td>2<br>(<span title="-0.2349%">-0.23%</span>)</td>
							</tr>
			<tr>
				<th class=""><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/slide.png"><br>-<span title="0.0000%">0.00%</span> (<span title="12.5073%">12.51%</span>)</th>
									<td>71</td>
					<td>0</td>
					<td>0</td>
					<td>0</td>
					<td>0</td>
							</tr>
			<tr>
				<th class=""><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/touch.png"><br>-<span title="0.0000%">0.00%</span> (<span title="2.6424%">2.64%</span>)</th>
									<td>42</td>
					<td>3</td>
					<td>0</td>
					<td>0</td>
					<td>0</td>
							</tr>
			<tr>
				<th class=""><img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/break.png"><br>-<span title="1.3744%">1.37%</span> (<span title="23.6072%">23.61%</span>)</th>
									<td>38</td>
					<td>30&nbsp;(22,8)<br>(<span title="-0.1234%">-0.12%</span>)</td>
					<td>7<br>(<span title="-0.7592%">-0.76%</span>)</td>
					<td>1<br>(<span title="-0.1853%">-0.19%</span>)</td>
					<td>1<br>(<span title="-0.3066%">-0.31%</span>)</td>
							</tr>
		</tbody></table>
		<div class="playlog_rating_detail_block f_r t_l">
			<div class="p_r p_3 p_l_0 f_l">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/rating_base_rainbow.png?ver=1.30" class="h_30 f_r">
				<div class="rating_block">15017</div>
			</div>
								<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/rating_keep.png" class="h_20 m_t_10 f_r">
						<div class="t_r f_0">
				<span class="f_l f_11 v_t">(+0)</span>
							</div>
		</div>
		<div class="clearfix m_b_5"></div>
		<div class="col2 f_l t_l f_0">
			<div class="playlog_score_block p_5">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/maxcombo.png" class="h_20">
				<div class="f_r f_14 white">459/1169</div>
			</div>
		</div>
		<div class="col2 p_l_5 f_l t_l f_0">
			<div class="playlog_score_block p_5">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/playlog/maxsync.png" class="h_20">
				<div class=" f_r f_14 white">747/2338</div>
			</div>
		</div>
		<div class="clearfix"></div>
	</div>


												<span class="playlog_master_container w_120 p_3 d_ib f_0">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/diff_master.png" class="h_16">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/icon_each.png" class="h_14 f_r">
				<div class="basic_block p_3 t_c f_11">ＧＵＥＳＴ</div>
			</span>
							<span class="gray_block w_120 p_3 d_ib f_0 ">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/icon_each.png" class="h_16 f_r">
				<div class="clearfix"></div>
				<div class="basic_block p_3 t_c f_11">―</div>
			</span>
							<span class="gray_block w_120 p_3 d_ib f_0 ">
				<img src="https://maimaidx-eng.com/maimai-mobile/img/icon_each.png" class="h_16 f_r">
				<div class="clearfix"></div>
				<div class="basic_block p_3 t_c f_11">―</div>
			</span>
				<div class="f_r p_t_10 d_ib f_0" id="matchingCtrl">
			<img src="https://maimaidx-eng.com/maimai-mobile/img/btn_off.png" class="h_30 m_t_5 m_b_5">
		</div>
		<div class="clearfix"></div>
	
'''

def get_score_data(html, debug=False):
    data_list = []
    for html_block in html:
        combo, sync, place = None, None, None
        players = 1

        soup = BeautifulSoup(html_block, "html.parser")
        # Get the score
        score = soup.find("div", {"class": "playlog_achievement_txt t_r"}).text
        # Get the song title
        title = soup.find("div", {"class": "basic_block m_5 p_5 p_l_10 f_13 break"}).text
        # Get the difficulty master
        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_master.png'})
        if diff:
            difficulty = 'MASTER'
        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_remaster.png'})
        if diff:
            difficulty = 'REMASTER'
        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_expert.png'})
        if diff:
            difficulty = 'EXPERT'
        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_advanced.png'})
        if diff:
            difficulty = 'ADVANCED'
        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_basic.png'})
        if diff:
            difficulty = 'BASIC'
        
        # Get the combo badge
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fcplus.png?ver=1.30'})
        if comb:
            combo = 'FC+'
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fc.png?ver=1.30'})
        if comb:
            combo = 'FC'
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/ap.png?ver=1.30'})
        if comb:
            combo = 'AP'
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/applus.png?ver=1.30'})
        if comb:
            combo = 'AP+'

        if debug:
            print(f"Combo: {combo}")

        # Get the 2p 1st or 2nd place badge
        plac1 = soup.find("img", {"class": "playlog_matching_icon f_r", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/2nd.png'})
        if plac1:
            place = '2nd'
            players = 2
        
        plac2 = soup.find("img", {"class": "playlog_matching_icon f_r", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/1st.png'})
        if plac2:
            place = '1st'
            players = 2

        # Check if the score is a new record deluxe
        new_record_deluxe = soup.find("img", {"class": "playlog_deluxscore_newrecord", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/newrecord.png'})
        if new_record_deluxe:
            new_record_deluxe = True
        else:
            new_record_deluxe = False
        
        # Check if the score is a new record
        new_record = soup.find("img", {"class": "playlog_achievement_newrecord", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/newrecord.png'})
        if new_record:
            new_record = True
        else:
            new_record = False

        # Get the 2p combo badge
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fsplus.png?ver=1.30'})
        if syn:
            sync = 'FS+'
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fs.png?ver=1.30'})
        if syn:
            sync = 'FS'
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fsd.png?ver=1.30'})
        if syn:
            sync = 'FSD'
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fsdplus.png?ver=1.30'})
        if syn:
            sync = 'FSD+'

        if debug:
            print(f"Sync: {sync}")

        # Get crit perfects
        td_list = soup.find_all('td')



        cp_taps = int(td_list[0].text)
        cp_holds = int(td_list[1].text)
        cp_slides = int(td_list[2].text.split('\n')[0])
        cp_touches = int(td_list[3].text.split('\n')[0])
        cp_breaks = int(td_list[4].text.split('\n')[0])

        # Get perfects



        # Get perfect % loss
        p_breaks_loss = soup.find('div', {'class': 'playlog_achievement_perfectloss'}).text.split('\n')[0]


        # Get the image link
        img_link = soup.find("img", {"class": "music_img m_5 m_r_0 f_l"})['src']
        # Get the dx score
        dx_score = soup.find("div", {"class": "white p_r_5 f_15 f_r"}).text
        type_img = soup.find('img', {'class': 'playlog_music_kind_icon', 'src': 'https://maimaidx-eng.com/maimai-mobile/img/music_standard.png'})
        if type_img:
            type = 'standard'
        else:
            type = 'dx'
        # Find all span elements inside the div element with class sub_title
        span_list = soup.find('div', {'class': 'sub_title'}).find_all('span')
        # Get the time/date (second span element)
        time = span_list[1].text
        # Get the track (first span element)
        track = span_list[0].text
        
        if debug:
            #print(f"Difficulty: {diff.upper()}")
            #print(f"Title: {title}")
            #print(f"Score: {score}")
            #print(f"Deluxe Score: {dx_score}")
            ...

        child_dict = {
            'title': title,
            'difficulty': difficulty,
            'score': score,
            'deluxe_score': dx_score,
            'type': type,
            'time': time,
            'track': track,
            'img_link': img_link,
            'combo': combo,
            'sync': sync,
            'place': place,
            'players': players,
            'new_record': new_record,
            'new_record_deluxe': new_record_deluxe
        }
        data_list.append(child_dict)
    return data_list

with open('test.txt', 'w') as f:
    f.write(get_score_data(html))