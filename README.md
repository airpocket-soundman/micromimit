# micromimit
たのしいmicrobitコンテスト2023エントリー作品「micro耳it」  
  
このリポジトリは、otama作、「micro耳it」のソース保管場所です。  

作品紹介  
https://www.youtube.com/watch?v=DAX19flW3io  
　
# src
開発環境はmicrobit python editorです  

## idou.py
音センシングを行う送信側のmicrobit用。  
idou = 移動の意味。トースターや電子レンジなどいまから音が鳴ることがわかる家電に使う端末。  
番号でどの家電に設置するかを選んでから音が鳴る部位に置いておく。  
  
## kotei.py
音センシングを行う送信側のmicrobit用。  
kotei = 固定の意味。冷蔵庫の開けっ放しの警報や、インターフォンなどいつ音がなるかわからない家電には常にこの端末を取り付けておく。  

## jyushin.py
音が鳴った情報を受信して、見取り図上のLEDを点灯する。  
目覚しのコントローラーとしても使用する。  
