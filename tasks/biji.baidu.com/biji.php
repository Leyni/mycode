<?php
    header('Content-type: text/html; charset=UTF8');

    $cookie = '__cfduid=d3b578259b6a9bdeb0454eee81f9e56071459000161; BAIDUID=3CAD3B6116E52167EFCA4373791033D1:FG=1; PSTM=1482485203; BIDUPSID=2B445FE172F45B6778C14A4FD573A864; MCITY=-131%3A; BDUSS=mVNdGk2aERSVnRiN09qcUM3WkFUdDI3SWFaN1QzUzlMWVotb2xyUk1ZLVJLSmhZSVFBQUFBJCQAAAAAAAAAAAEAAABG~c4AwfrZ7QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJGbcFiRm3BYT; userid=13565254; token_=821663c85351575457505756102ab60c6c6ee6d5af9d8e96dfd92c6936ba9654; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2; H_PS_PSSID=1455_19035_21087_21943_17001_20698; cflag=15%3A3; Hm_lvt_3cf279110e3531abf3c2e9e987ea0ec7=1482073693,1484104289; Hm_lpvt_3cf279110e3531abf3c2e9e987ea0ec7=1484300466';


    if (isset($_GET['notebook_id'])) {
        $notebook_id = $_GET['notebook_id'];
    } else {
        $notebook_id = '1923177';
    }

    $page_num = 0;
    $page_size = 15;
    $content = array();

    do {
        $page_num++;

        $post_data = 'source_type=PC&page_num='.$page_num.'&page_size='.$page_size.'&notebook_id='.$notebook_id.
            '&order_by=agent_update_time&order_type=desc';
        $ch = curl_init('http://biji.baidu.com/inotes/api/note_list');
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 3000);
        curl_setopt($ch, CURLOPT_TIMEOUT, 3000);
        curl_setopt($ch, CURLOPT_COOKIE, $cookie);
        curl_setopt($ch, CURLOPT_POST, true); 
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);

        $result = json_decode(curl_exec($ch), true);

        foreach ($result['data']['notes'] as $item) {
            $content []= $item['source'];
        }

        $total_page = $result['pagination']['total_page'];

    } while($page_num < $total_page and $page_num * $page_size <= 50);

    $content = array_reverse($content);

    $html = '<html> <body> '; 
    foreach ($content as $note) {
        $html.= $note.'<br><br>';
    }
    
    $html.= '</body> </html>';
    echo $html;
?>
