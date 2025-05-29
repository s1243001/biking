
import streamlit as st
import leafmap.foliumap as leafmap

st.title("選擇你的路段")

option = st.selectbox(
    '選擇你的路段',
    ['台北-新竹', '新竹-台中', '台中-嘉義', '嘉義-高雄','高雄-屏東','屏東-台東','台東-花蓮','花蓮-宜蘭','宜蘭-台北'])
st.text(f'你的答案：{option}')

if option == '台北-新竹':
    t_s = "taipei_hsinchu.geojson"
    m = leafmap.Map(center = [121.182838, 24.949132], zoom = 7 , minimap_control=True)
    m.add_geojson(t_s, layer_name="台北-新竹", style=style)
else if option == '新竹-台中':
        s_tc = "hsinchu_taichung.geojson"
        m = leafmap.Map(center = [120.740153, 24.462711], zoom = 7 , minimap_control=True)
        m.add_geojson(s_tc, layer_name="新竹-台中", style=stlye)
else if option == '台中-嘉義':
        tc_jia = "taichung_jiayi.geojson"
        m = leafmap.Map(center = [120.292326, 23.809488], zoom = 7 , minimap_control=True)
        m.add_geojson(tc_jia, layer_name="台中-嘉義", style=style)
else if option == '嘉義-高雄':
        jia_kao = "jiayi_kaohsung.geojson"
        m = leafmap.Map(center = [120.148435, 22.999866], zoom = 7 , minimap_control=True)
        m.add_geojson(jia_kao, layer_name="嘉義-高雄", style=style)
else if option == '高雄-屏東':
        kao_ping = 'kaohsung_pingtung.geojson'
        m = leafmap.Map(center = [120.536198, 22.402317], zoom = 7 , minimap_control=True)
        m.add_geojson(kao_ping, layer_name="高雄-屏東", style=style)
else if option == '屏東-台東':
        ping_tait = "pingtung_taitung.geojson"
        m = leafmap.Map(center = [120.834135, 22.781440], zoom = 7, minimap_control = True)
        m.add_geojson(ping_tait, layer_name="屏東-台東", style=syle)
else if option == '台東-花蓮':
        tait_hua = "taitung_huaien.geojson"
        m = leafmap.Map(center = [121.335207, 23.429920], zoom = 7, minimap_control = True)
        m.add_geojson(tait_hua, layer_name="台東-花蓮", style=style)
else if option == '花蓮-宜蘭':
        hua_yi = "hualien_yilan.geojson"
        m = leafmap.Map(center = [121.532195, 24.228917], zoom = 7, minimap_control = True)
        m.add_geojson(hua_yi, layer_name="花蓮-宜蘭", style=style)
else if option == '宜蘭-台北':
        yi_taip = "yilan_taipei.geojson"
        m = leafmap.Map(center = [121.675311, 24.899394], zoom = 7, minimap_control = True)
        m.add_geojson(yilan_taip, layer_name="宜蘭-台北", style=style)

m.to_streamlit(height=700)
