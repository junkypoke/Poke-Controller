【注意点】
・Anacondaインストール先を変更している場合、
  「0_CreatEnv～.bat」を編集し、
  「batfile」のダブルクオーテーションの中を適宜変更してください
  (デフォルトC:\Users\(user)\Anaconda3\Scripts\activate.bat)
・「0_CreatEnv～.bat」と「1_OpenWindow～.bat」に記載のある「ProjectName」は必ず一致させてください。
・ファイル名に「_36」がついているものはPython3.6向け、ファイル名に「_37」がついているものはPython3.7向けです。
  ※Poke-ControllerはPython3.6推奨ですが、拡張機能によりPython3.7が必要になることを想定

【下準備】
① 「格納方法.png」を参考にファイルをPoke-Controllerに格納する
② 0_CreatEnv～.batを1回ポチる

【本編】
① Poke-Controllerを起動したいときに「1_OpenWindow～.bat」をポチる

【備考】
・「install_bat」フォルダにインストール用のバッチファイルが入っているので、
  インストール用のバッチを増やす事により、まとめてインストールしてくれます。
  「Default_～.bat」はPoke-Controllerに必須なライブラリ、
  「Option_～.bat」は拡張機能用のライブラリになっています。

【batファイル簡易解説】
■必須
Default_opencv-python.bat				コンピュータビジョンライブラリ
Default_Pillow.bat						画像処理ライブラリ
Default_pynput.bat						キーボードやマウス操作を行うライブラリ
Default_pyserial.bat					シリアル通信用ライブラリ
Default_pythonnet(_36 or _37).bat		NETを呼び出すライブラリ

■任意
Option_numpy.bat						数値計算をより高速に、効率的に行うライブラリ
Option_pandas.bat						データ解析ライブラリ
Option_pygubu.bat						インタフェースライブラリ
Option_pyocr.bat						文字認識用ライブラリ
Option_requests.bat						HTTPライブラリ
Option_plyer.bat						デスクトップ通知用ライブラリ


【変更履歴】
v01	: 初版
v02	: ■0_CreatEnv.bat
	  ・「install_bat」フォルダを作成し、インストール用のバッチファイルを分離
v03	: 「install_bat」フォルダに「pyocr.bat」を追加
v04	: ・「install_bat」フォルダに格納されているバッチファイルをリネーム
	     (ファイル名に「Default_」、「Option_」を付与)
	  ・「install_bat」フォルダに「Option_requests.bat」を追加
v05	: ・「Option_numpy.bat」、「Option_pandas.bat」、「Option_pygubu.bat」を追加
	  ・【batファイル簡易解説】追加
v06	: ・Python3.6とPython3.7を両立できるようにファイル構成の見直し
v07	: ・Option_plyer.bat追加

【作成者】
ろっこく(Twitter) : @Rokkoku_I