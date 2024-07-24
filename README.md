# 파이썬 기반의 도서관 출납 서비스

### 사전에 구상한 도서관 출납 서비스 설계 다이어그램
![도서 대출 시스템](https://github.com/user-attachments/assets/591bb57f-288a-4350-9610-58111f5f5181)


#### 프로젝트 : 파이썬 기반의 도서관 출납 서비스
#### 기한 : 7.22 ~ 7.25

#### 프로젝트의 설명과 목적  

-위에 표에서 구상한 것처럼 일반 사용자와 관리자의 탭을 나눠 도서 대출 시스템과 관리자의 데이터 처리 기능을 구현하고 싶었습니다. 

-관리자의 기능에 접속하려면 올바른 비밀번호를 입력해야 접속이 가능하게 구상하고 싶었습니다.

#### 세부사항 

-미리 설계 다이어그램을 짜두어서 상향식 설계 방식이 어울릴 것이라 생각해 첫번째 기능인 도서 정보 관리 기능을 만들어 보았습니다.

-먼저 Book.py와 BookManager.py로 나누었습니다.

-Book 클래스 안에는 도서들의 정보들과 실제 화면 구성들에 필요한 내용들을 기입했습니다.

-BookManager 클래스 안에는 도서라는 데이터를 추가, 수정, 삭제, 전체 도서 확인 기능에 필요한 내용들을 기입했습니다. 

#### 프로젝트 요약 및 개선사항

-먼저 관리자 기능을 먼저 구현하고 대출 기능(일반 사용자)을 마저 구현하려 했지만, 능력 부족으로 관리자 기능을 완성을 시키지 못한 관계로 도서 대출 기능의 설계는 시작하지도 못했습니다.

-아직 구현되지 못한 기능들 도서관 정보, 회원 정보, 대출/반납 정보는 앞서 했던 도서 정보 관리랑 비슷한 면이 많으므로 복습하고 익숙해지기 위해 기능을 구현 할 계획입니다.

-아직 설계되지 못한 도서 대출 기능과 비밀번호를 통해 관리자 기능에 접근하는 기능을 만들어 볼 계획입니다.

-대출 중인 도서, 연체 중인 도서, 반납 한 도서의 데이터 처리 방법을 고민하여 도서 정보, 회원 정보랑도 연결시켜 볼 계획입니다.
