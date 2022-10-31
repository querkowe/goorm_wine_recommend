# 와인 검색 & 추천 기능

## 개요

와인 이름을 기반으로 데이터베이스에서 검색하여 와인의 정보와 이를 기반으로 추천된 다른 와인을 보여줍니다

## 필요 라이브러리

- selenium(4.1.0)
- webdriver-manager(3.5.2)

## 흐름

1. 사용자는 가격대(고가, 중가, 저가)와 와인 이름을 입력합니다
  - 현재 와인 이름을 정확하게 입력하지 않으면 검색할 수 없는 문제가 있고 해결중입니다
1. 입력한 정보를 바탕으로 데이터베이스에서 와인의 상세정보를 가져옵니다
1. 와인의 상세정보 내의 와인의 id를 통해 미리 구해놓은 추천 와인의 id 목록을 가져옵니다
1. 추천 와인의 id로 추천 와인의 이름을 묶어서 이를 웹페이지에 표시합니다
  - 사진을 표시하는 기능을 구현중입니다
1. 추천 와인의 이름으로 다시 와인의 상세정보를 볼 수 있습니다