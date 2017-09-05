<?php
    header('Content-type: text/html; charset=UTF8');

    $user = $_GET['user'];
    if (isset($_GET['year'])) {
        $req_year = $_GET['year'];
    } else {
        $req_year = date("Y");
    }

    $start = -100;
    $count = -$start;

    $stat_array = array();
    $lastest_array = array();

    do {
        $start += $count;

        $ch = curl_init('https://api.douban.com/v2/book/user/'.$user.'/collections?status=read&start='.$start.'&count='.$count);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 3000);
        curl_setopt($ch, CURLOPT_TIMEOUT, 3000);

        $result = json_decode(curl_exec($ch), true);

        $total = $result['total'];

        foreach ($result['collections'] as $item) {
            $year = substr($item['updated'], 0, 4);
            if (!isset($stat_array[$year])) {
                $stat_array[$year] = array(
                    'read_cnt' => 0,
                    'score_sum' => 0,
                    'tag_list' => array()
                );
            }
            $stat_array[$year]['read_cnt'] += 1;
            $stat_array[$year]['score_sum'] += $item['rating']['value'];

            foreach ($item['tags'] as $tag) {
                if (!isset($stat_array[$year]['tag_list'][$tag])) {
                    $stat_array[$year]['tag_list'][$tag] = 1; 
                } else {
                    $stat_array[$year]['tag_list'][$tag] += 1; 
                }
            }

            if ($year === $req_year) {
                $lastest_array[] = array(
                    'title' => $item['book']['title'],
                    'score' => $item['rating']['value'],
                    'time' => $item['updated'],
                );
            }
        }
    } while($start + $count < $total);
    

    $html = "<html> <body> <table border=\"1\"> <tr> <th>${req_year}年的读书清单</th> </tr> "; 
    $html.= '<tr> <th>书名</th> <th>评分</th> <th>更新时间</th> ';
    foreach ($lastest_array as $book) {
        $html.= '<tr> <td>'.$book['title'].'</td> <td>'.$book['score'].'</td> <td>'.$book['time'].'</td> <tr>';
    }
    $html.= '</table>';
    $html.= '<br><br>';

    foreach ($stat_array as $year => $item) {
        $html.= '<table border="1">';
        $html.= '<tr> <th>'.$year.'年读书汇总</th> </tr>';
        $html.= '<tr> <th>阅读量</th> <td>'.$item['read_cnt'].'</td> </tr>';
        $html.= '<tr> <th>平均评分</th> <td>'.round($item['score_sum'] / $item['read_cnt'], 1).'</td> </tr>';
        //echo "其中tag包括：\n";
        //foreach ($item['tag_list'] as $tag_name => $tag_cnt) {
        //    echo $tag_name."（".$tag_cnt."）\t";
        //}
        $html.= '</table>';
        $html.= '<br><br>';
    }

    //var_dump($stat_array); var_dump($lastest_array); exit();
    
    $html.= '</body> </html>';
    echo $html;
?>
