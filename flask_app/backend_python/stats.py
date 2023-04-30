import os
import json
import collections

class overview_stats:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def test(self):
        print(162)

    def get_stats_data(self):
        data = []
        files = os.listdir(self.file_path)
        #print(files)
        for file in files:
            if file.endswith('.json'):
                #print(file)
                with open(self.file_path + '\\' + file, 'r') as f:
                    data.append(json.load(f))
        self.data = data
    
    def calculate_stats(self):
        #print(len(self.data))
        c = collections.defaultdict(int)

        #init count variables
        level_count = c
        int_level_count = c

        title_count = c
        type_count = c
        difficulty_count = c

        total_taps_count = c
        total_holds_count = c
        total_slides_count = c
        total_touch_count = c
        total_breaks_count = c

        total_score_count = c
        total_deluxe_score_count = c
        total_combo_count = c
        total_sync_count = c
        total_max_combo_count = c
        total_max_sync_count = c
        new_record_count = c
        new_record_deluxe_count = c
        rating_gain_count = c
        current_rating_count = c
        fast_count = c
        late_count = c

        place_count = c
        players_count = c
        player2_count = c

        track_count = c

        #init avg variables
        internal_level_data = []
        internal_level_data_none = []
        all_note_type_ratio_data = []
        taps_ratio_data = []
        holds_ratio_data = []
        slides_ratio_data = []
        touch_ratio_data = []
        breaks_ratio_data = []

        #custom variables
        #count each level and internal level p2 picks
        p2_picks = {}
        p2_picks_count = c
        parent_p2_picks = []
        p2_level_picks = {}


        chart_count = 0
        for day in self.data:
            #print(len(day))
            for chart in day:

                #init chart attributes
                title = chart['title']
                difficulty = chart['difficulty']
                score = chart['score']
                deluxe_score = chart['deluxe_score']
                type = chart['type']
                time = chart['time']
                track = chart['track']
                img_link = chart['img_link']
                combo = chart['combo']
                sync = chart['sync']
                place = chart['place']
                players = chart['players']
                new_record = chart['new_record']
                new_record_deluxe = chart['new_record_deluxe']
                taps = chart['taps']
                cp_taps = chart['taps']['critical_perfect']
                p_taps = chart['taps']['perfect']
                gr_taps = chart['taps']['great']
                go_taps = chart['taps']['good']
                m_taps = chart['taps']['miss']
                holds = chart['holds']
                cp_holds = chart['holds']['critical_perfect']
                p_holds = chart['holds']['perfect']
                gr_holds = chart['holds']['great']
                go_holds = chart['holds']['good']
                m_holds = chart['holds']['miss']
                slides = chart['slides']
                cp_slides = chart['slides']['critical_perfect']
                p_slides = chart['slides']['perfect']
                gr_slides = chart['slides']['great']
                go_slides = chart['slides']['good']
                m_slides = chart['slides']['miss']
                touch = chart['touch']
                cp_touch = chart['touch']['critical_perfect']
                p_touch = chart['touch']['perfect']
                gr_touch = chart['touch']['great']
                go_touch = chart['touch']['good']
                m_touch = chart['touch']['miss']
                breaks = chart['breaks']
                cp_breaks = chart['breaks']['critical_perfect']
                p_breaks = chart['breaks']['perfect']
                gr_breaks = chart['breaks']['great']
                go_breaks = chart['breaks']['good']
                m_breaks = chart['breaks']['miss']
                player2 = chart['player2']
                max_combo = chart['max_combo']
                max_sync = chart['max_sync']
                rating_gain = chart['rating_gain']
                current_rating = chart['current_rating']
                fast = chart['fast']
                late = chart['late']
                internal_level = chart['internal_level']
                level = chart['level']


                #Count total charts
                chart_count += 1

                #Basic count stats
                #Get level stats
                level_count[level] += 1
                int_level_count[internal_level] += 1

                #Get chart stats
                title_count[title] += 1
                type_count[type] += 1
                difficulty_count[difficulty] += 1

                #Get note stats
                total_taps = sum(taps.values())
                total_holds = sum(holds.values())
                total_slides = sum(slides.values())
                total_touch = sum(touch.values())
                total_breaks = sum(breaks.values())

                total_taps_count[total_taps] += 1
                total_holds_count[total_holds] += 1
                total_slides_count[total_slides] += 1
                total_touch_count[total_touch] += 1
                total_breaks_count[total_breaks] += 1

                #Get user play stats
                total_score_count[score] += 1
                total_deluxe_score_count[deluxe_score] += 1
                total_combo_count[combo] += 1
                total_sync_count[sync] += 1
                total_max_combo_count[max_combo] += 1
                total_max_sync_count[max_sync] += 1
                new_record_count[new_record] += 1
                new_record_deluxe_count[new_record_deluxe] += 1
                rating_gain_count[rating_gain] += 1
                current_rating_count[current_rating] += 1
                fast_count[fast] += 1
                late_count[late] += 1

                #Get multiplayer stats
                place_count[place] += 1
                players_count[players] += 1
                player2_count[player2] += 1

                #Get misc stats
                track_count[track] += 1

                #Avg stat prep
                #Avg internal level
                if internal_level != None:
                    internal_level_data.append(float(internal_level))
                    internal_level_data_none.append(float(internal_level))
                else:
                    internal_level_data_none.append(0)
                
                #Avg all note type ratio
                total_notes = total_taps + total_holds + total_slides + total_touch + total_breaks
                total_cp = cp_taps + cp_holds + cp_slides + cp_touch + cp_breaks
                total_p = p_taps + p_holds + p_slides + p_touch + p_breaks
                total_gr = gr_taps + gr_holds + gr_slides + gr_touch + gr_breaks
                total_go = go_taps + go_holds + go_slides + go_touch + go_breaks
                total_m = m_taps + m_holds + m_slides + m_touch + m_breaks

                cp_ratio = total_cp / total_notes
                p_ratio = total_p / total_notes
                gr_ratio = total_gr / total_notes
                go_ratio = total_go / total_notes
                m_ratio = total_m / total_notes

                all_note_type_ratio_data.append([cp_ratio, p_ratio, gr_ratio, go_ratio, m_ratio])

                #Avg taps ratio
                cp_taps_ratio = cp_taps / total_taps
                p_taps_ratio = p_taps / total_taps
                gr_taps_ratio = gr_taps / total_taps
                go_taps_ratio = go_taps / total_taps
                m_taps_ratio = m_taps / total_taps

                taps_ratio_data.append([cp_taps_ratio, p_taps_ratio, gr_taps_ratio, go_taps_ratio, m_taps_ratio])

                #Avg holds ratio
                cp_holds_ratio = cp_holds / total_holds
                p_holds_ratio = p_holds / total_holds
                gr_holds_ratio = gr_holds / total_holds
                go_holds_ratio = go_holds / total_holds
                m_holds_ratio = m_holds / total_holds

                holds_ratio_data.append([cp_holds_ratio, p_holds_ratio, gr_holds_ratio, go_holds_ratio, m_holds_ratio])

                #Avg slides ratio
                cp_slides_ratio = cp_slides / total_slides
                p_slides_ratio = p_slides / total_slides
                gr_slides_ratio = gr_slides / total_slides
                go_slides_ratio = go_slides / total_slides
                m_slides_ratio = m_slides / total_slides

                slides_ratio_data.append([cp_slides_ratio, p_slides_ratio, gr_slides_ratio, go_slides_ratio, m_slides_ratio])

                #Avg touch ratio
                if total_touch > 0:
                    cp_touch_ratio = cp_touch / total_touch
                    p_touch_ratio = p_touch / total_touch
                    gr_touch_ratio = gr_touch / total_touch
                    go_touch_ratio = go_touch / total_touch
                    m_touch_ratio = m_touch / total_touch

                    touch_ratio_data.append([cp_touch_ratio, p_touch_ratio, gr_touch_ratio, go_touch_ratio, m_touch_ratio])

                #Avg breaks ratio
                cp_breaks_ratio = cp_breaks / total_breaks
                p_breaks_ratio = p_breaks / total_breaks
                gr_breaks_ratio = gr_breaks / total_breaks
                go_breaks_ratio = go_breaks / total_breaks
                m_breaks_ratio = m_breaks / total_breaks

                breaks_ratio_data.append([cp_breaks_ratio, p_breaks_ratio, gr_breaks_ratio, go_breaks_ratio, m_breaks_ratio])
                
                #Custom
                if player2 not in p2_picks:
                    p2_picks[player2] = {}

                if player2 != None:
                    if level not in p2_picks[player2]:
                        p2_picks[player2][level] = 1
                    else:
                        p2_picks[player2][level] += 1

                    if internal_level not in p2_picks[player2]:
                        p2_picks[player2][internal_level] = 1
                    else:
                        p2_picks[player2][internal_level] += 1


                
                


        #Avg stat calculations
        #internal level
        avg_internal_level = sum(internal_level_data) / len(internal_level_data)
        avg_internal_level_none = sum(internal_level_data_none) / len(internal_level_data_none)

        #all note type ratio
        avg_cp_ratio = sum([x[0] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_p_ratio = sum([x[1] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_gr_ratio = sum([x[2] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_go_ratio = sum([x[3] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_m_ratio = sum([x[4] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)

        #taps ratio
        avg_cp_taps_ratio = sum([x[0] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_p_taps_ratio = sum([x[1] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_gr_taps_ratio = sum([x[2] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_go_taps_ratio = sum([x[3] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_m_taps_ratio = sum([x[4] for x in taps_ratio_data]) / len(taps_ratio_data)

        #holds ratio
        avg_cp_holds_ratio = sum([x[0] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_p_holds_ratio = sum([x[1] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_gr_holds_ratio = sum([x[2] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_go_holds_ratio = sum([x[3] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_m_holds_ratio = sum([x[4] for x in holds_ratio_data]) / len(holds_ratio_data)

        #slides ratio
        avg_cp_slides_ratio = sum([x[0] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_p_slides_ratio = sum([x[1] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_gr_slides_ratio = sum([x[2] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_go_slides_ratio = sum([x[3] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_m_slides_ratio = sum([x[4] for x in slides_ratio_data]) / len(slides_ratio_data)

        #touch ratio
        avg_cp_touch_ratio = sum([x[0] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_p_touch_ratio = sum([x[1] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_gr_touch_ratio = sum([x[2] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_go_touch_ratio = sum([x[3] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_m_touch_ratio = sum([x[4] for x in touch_ratio_data]) / len(touch_ratio_data)

        #breaks ratio
        avg_cp_breaks_ratio = sum([x[0] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_p_breaks_ratio = sum([x[1] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_gr_breaks_ratio = sum([x[2] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_go_breaks_ratio = sum([x[3] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_m_breaks_ratio = sum([x[4] for x in breaks_ratio_data]) / len(breaks_ratio_data)

            
        #print('Count Stats:')
        #print('Level:', level_count)
        #print('Internal Level:', int_level_count)

        #print('Title:', title_count)
        #print('Type:', type_count)
        #print('Difficulty:', difficulty_count)
#
        #print('Total Taps:', total_taps_count)
        #print('Total Holds:', total_holds_count)
        #print('Total Slides:', total_slides_count)
        #print('Total Touch:', total_touch_count)
        #print('Total Breaks:', total_breaks_count)
#
        #print('Total Score:', total_score_count)
        #print('Total Deluxe Score:', total_deluxe_score_count)
        #print('Total Combo:', total_combo_count)
        #print('Total Sync:', total_sync_count)
        #print('Total Max Combo:', total_max_combo_count)
        #print('Total Max Sync:', total_max_sync_count)
        #print('New Record:', new_record_count)
        #print('New Record Deluxe:', new_record_deluxe_count)
        #print('Rating Gain:', rating_gain_count)
        #print('Current Rating:', current_rating_count)
        #print('Fast:', fast_count)
        #print('Late:', late_count)
#
        #print('Place:', place_count)
        #print('Players:', players_count)
        #print('Player2:', player2_count)
#
        #print('Track:', track_count)
#
        #print('Avg Stats:')
        #print('Avg Internal Level:', avg_internal_level)
        #print('Avg Internal Level None:', avg_internal_level_none)
#
        #print(f'Avg Critical Perfect Ratio:{avg_cp_ratio*100}%')
        #print(f'Avg Perfect Ratio:{round(avg_p_ratio*100, 2)}%')
        #print(f'Avg Great Ratio:{round(avg_gr_ratio*100, 2)}%')
        #print(f'Avg Good Ratio:{round(avg_go_ratio*100, 2)}%')
        #print(f'Avg Miss Ratio:{round(avg_m_ratio*100, 2)}%')
#
        #print(f'Avg Critical Perfect Taps Ratio:{round(avg_cp_taps_ratio*100, 2)}%')
        #print(f'Avg Perfect Taps Ratio:{round(avg_p_taps_ratio*100, 2)}%')
        #print(f'Avg Great Taps Ratio:{round(avg_gr_taps_ratio*100, 2)}%')
        #print(f'Avg Good Taps Ratio:{round(avg_go_taps_ratio*100, 2)}%')
        #print(f'Avg Miss Taps Ratio:{round(avg_m_taps_ratio*100, 2)}%')
    #
        #print(f'Avg Critical Perfect Holds Ratio:{round(avg_cp_holds_ratio*100, 2)}%')
        #print(f'Avg Perfect Holds Ratio:{round(avg_p_holds_ratio*100, 2)}%')
        #print(f'Avg Great Holds Ratio:{round(avg_gr_holds_ratio*100, 2)}%')
        #print(f'Avg Good Holds Ratio:{round(avg_go_holds_ratio*100, 2)}%')
        #print(f'Avg Miss Holds Ratio:{round(avg_m_holds_ratio*100, 2)}%')
#
        #print(f'Avg Critical Perfect Slides Ratio:{round(avg_cp_slides_ratio*100, 2)}%')
        #print(f'Avg Perfect Slides Ratio:{round(avg_p_slides_ratio*100, 2)}%')
        #print(f'Avg Great Slides Ratio:{round(avg_gr_slides_ratio*100, 2)}%')
        #print(f'Avg Good Slides Ratio:{round(avg_go_slides_ratio*100, 2)}%')
        #print(f'Avg Miss Slides Ratio:{round(avg_m_slides_ratio*100, 2)}%')
#
        #print(f'Avg Critical Perfect Touch Ratio:{round(avg_cp_touch_ratio*100, 2)}%')
        #print(f'Avg Perfect Touch Ratio:{round(avg_p_touch_ratio*100, 2)}%')
        #print(f'Avg Great Touch Ratio:{round(avg_gr_touch_ratio*100, 2)}%')
        #print(f'Avg Good Touch Ratio:{round(avg_go_touch_ratio*100, 2)}%')
        #print(f'Avg Miss Touch Ratio:{round(avg_m_touch_ratio*100, 2)}%')
#
        #print(f'Avg Critical Perfect Breaks Ratio:{round(avg_cp_breaks_ratio*100, 2)}%')
        #print(f'Avg Perfect Breaks Ratio:{round(avg_p_breaks_ratio*100, 2)}%')
        #print(f'Avg Great Breaks Ratio:{round(avg_gr_breaks_ratio*100, 2)}%')
        #print(f'Avg Good Breaks Ratio:{round(avg_go_breaks_ratio*100, 2)}%')
        #print(f'Avg Miss Breaks Ratio:{round(avg_m_breaks_ratio*100, 2)}%')
#
        #print(f'{p2_picks}')
#
        #print('Total Charts:', chart_count)

        print('p2_picks:', p2_picks)




        

instance = overview_stats(r'C:\Users\joshu\Documents\GitHub\Projects-Website\flask_app\records')

instance.get_stats_data()

instance.calculate_stats()