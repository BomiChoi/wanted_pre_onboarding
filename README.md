# 프리온보딩 백엔드 코스 선발과제

## 요구사항

1. 채용공고를 등록합니다.
2. 채용공고를 수정합니다.
3. 채용공고를 삭제합니다.
4. 채용공고 목록을 가져옵니다.
    * 채용공고 검색 기능 (선택)
5. 채용 상세 페이지를 가져옵니다. (선택)
    * 해당 회사가 올린 다른 채용공고 (선택)
6. 사용자는 채용공고에 지원합니다. (선택)

## 모델 설계

ERD - https://www.erdcloud.com/d/QSebd9ueurZkwimMS

## API 설계

| 요청 메소드     | URL                      | 설명                |
|------------|--------------------------|-------------------|
| GET        | /posts                   | 채용공고 목록을 가져옵니다.   |
| POST       | /posts                   | 채용공고를 등록합니다.      |
| GET        | /posts/&lt;id&gt;        | 채용 상세 페이지를 가져옵니다. |
| PUT, PATCH | /posts/&lt;id&gt;        | 채용공고를 수정합니다.      |
| DELETE     | /posts/&lt;id&gt;        | 채용공고를 삭제합니다.      |
| POST       | /applications            | 채용공고에 지원합니다.      |
| DELETE     | /applications/&lt;id&gt; | 채용공고 지원을 취소합니다.   |

## 사이트 링크

https://wanted-pre-onboading.herokuapp.com/