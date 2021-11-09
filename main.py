# CNUTomatoes Ver 0.1
# 내용
#   1) 네이버 영화에서 영화 리뷰 수집
#   2) 수집된 리뷰 MongoDB에 저장
#   3) MongoDB에서 수집된 리뷰 불러옴
#   4) 인공지능에서 사용할 수 있게 전처리
#   5) 전처리 된 데이터를 활용하여 인공지능 분석 시작
#   6) 분석결과를 시가고하
# 만든이 : 박지원
# 일자 : 2021년 11월 9일

import webcrawl.WebCrawlService as wcs

###########################
# 1. 데이터 수집 및 저장
###########################

movie_code = 209496

# 1. 제목 수집

title = wcs.get_movie_title(movie_code)
print(title)
