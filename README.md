# Poke-Controller plug-in
Poke-Controller用の自動化プラグインになります。<br>
追加したプログラムに関する問い合わせは、IssueまたはTwitter DM [@junky_poke](https://twitter.com/junky_poke_) まで。<br>
 
## 追加プログラム 
 
### 1.画像の閾値を確認するプログラム
用意した画像の閾値を調べるためのプログラムです。<br>
デフォルトでは、Network_Offline.pngの画像になっていますので、任意の画像に変更して使用ください。<br>
> File: IMG Check.py <br>
> Title: IMG_Check <br>
<br>
 
### 2.デリバードレイドの検索（星4/星5)
冠の雪原で、巣穴でレア柱を建てた後に使用できます。<br>
Switchの日付変更を可能にした状態で、巣穴の前で使用してください。<br>
> File: JPN_Delibird4_Search.py , JPN_Dlibird5_Search.py <br>
> Title: JPN_★4デリバードレイド検索, JPN_★5デリバードレイド検索 <br>
<br>
 
### 3.リポップでの色違い厳選プログラム(JPN/ENG/GER)
手持ちのポケモンを4匹以上にした状態で、固定シンボルのリポップの設定をしてください。<br>
ソフトウェアを起動したら自動でエンカウントできるリポップの設定ができたら、ゲームタイトル画面で使用してください。<br>
> File: JPN_Repop_Shiny.py, ENG_Repop_Shiny.py, GER_Repop_Shiny.py <br>
> Title: JPN_リポップ色違い厳選, ENG_リポップ色違い厳選, GER_リポップ色違い厳選 <br>
<br>
<br>

### 4.釣りでの色違い厳選
手持ちのポケモンを4匹以上にした状態で、釣り竿にかかった際のビックリマークが大きく見えるような角度で開始してください。<br>
<br>

### 5.ランダム・シンボルでの色違い厳選
ワイルドエリアの草むらでの色違い厳選用プログラムです。手持ちのポケモンを4匹以上にした状態で使用してください。<br>
草むらから出てしまう場合や長時間エンカウントがない場合の処理はまだ入れていないので今後修正します。<br>
<br>

### 6.空中でのリポップ個体の厳選
空中のポケモンのリポップ設定をしたのちに、手持ちのポケモンを4匹以上にした状態で使用してください。<br>
口笛を一定間隔で吹き呼び寄せながらエンカウントを待ちます。<br>
<br>


## インストール・起動用BATファイルの追加
ろっこく氏( https://twitter.com/Rokkoku_I )の開発によるインストール・起動用のBATファイルを追加しました。<br>
使用方法の詳細は、noteをご覧ください。( https://note.com/junky_poke_/n/n11e65b1b474b )<br>
また、最新版はを使用する際は、ろっこく氏のTwitterより入手してください。<br>


以下は、本家様の説明になります。
 
---

# Poke-Controller

Pythonで書く！Switchの自動化支援ソフトウェア

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## セットアップと使い方

- まずはモノの準備  
	- [Github - wiki](https://github.com/KawaSwitch/Poke-Controller/wiki)

- 準備ができたら進みましょう  
	- [Poke-Controllerの使い方](https://github.com/KawaSwitch/Poke-Controller/wiki/Poke-Controller%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9)

	- [デフォルトの実装コマンドの確認](https://github.com/KawaSwitch/Poke-Controller/wiki/%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%81%AE%E5%AE%9F%E8%A3%85%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)  

	- [新しいコマンドを作成](https://github.com/KawaSwitch/Poke-Controller/wiki/%E6%96%B0%E3%81%97%E3%81%84Python%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9)

分からないことや改善要望などがあれば遠慮なく[Issue](https://github.com/KawaSwitch/Poke-Controller/issues)まで  
[Q&A](https://github.com/KawaSwitch/Poke-Controller/wiki/Q&A)や[解決済みIssue](https://github.com/KawaSwitch/Poke-Controller/issues?q=is%3Aissue+is%3Aclosed)なども役に立つかもしれません  

## クイックビュー
簡単に機能を見てみましょう  

### コマンド作成用のライブラリの提供  

通常のボタン押下  
`self.press(Button.A) # Aボタンを押して離す`  
`self.press(Button.A, 0.1, 1) # Aボタンを0.1秒間押して離した後, 1秒待機`  

左右スティック & HAT(十字)キー  
`self.press(Direction.RIGHT, 5) # 左スティックを右に5秒間倒す`  
`self.press(Hat.LEFT) # 十字キー左を押して離す`  

同時押し  
`self.press([Button.A, Button.B]) # AボタンとBボタンを同時に押して離す`  

ホールド  
`self.hold([Direction.UP, Direction.R_DOWN], wait=1) # 左スティックを上, 右スティックを下に倒して1秒待つ`  
`self.press(Button.A) # スティックを倒した状態でAボタンを押して離す`  

[リファレンス](https://github.com/KawaSwitch/Poke-Controller/wiki/Python%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89_%E4%BD%9C%E6%88%90How_to)やデフォルトのコマンドなども参考にして中身を覗いてみましょう  
作成したコマンドや便利な機能は[プルリク](https://github.com/KawaSwitch/Poke-Controller/pulls)や[Issue](https://github.com/KawaSwitch/Poke-Controller/issues)で頂けると非常に喜びます  

### Pythonファイル管理  
作成したコマンドのclassは1つのPythonファイルの中にいくつも記述できます  
またPythonCommandsのフォルダ内であればいくつもフォルダを作成可能です  
自由に配置していきましょう  

![](https://github.com/KawaSwitch/Poke-Controller/blob/photo/photos/Wiki/PythonCommandHowTo/command_file_location.PNG)

### 実行時のコマンド切替  
配置したコマンド群はマウス操作で簡単に切り替えることができます  

### リロード機能  
Poke-Controllerを動作しながらファイルの変更を再読込して反映することができます  
こつこつデバグしたい方におすすめ！  

### 画像認識  

キャプチャボードでSwitchの画面を取り込めば, シリアル通信だけでは叶わない操作もできるかも  
これらもライブラリとして機能を提供しています  
`self.isContainTemplate('status.png') # テンプレートマッチング`  

現在の機能([実装内容](https://github.com/KawaSwitch/Poke-Controller/wiki/%E7%94%BB%E5%83%8F%E8%AA%8D%E8%AD%98%E3%81%A8%E3%81%AF))は少ないがアップデート予定  
![リリース前GUI](https://github.com/KawaSwitch/Poke-Controller/blob/photo/photos/pokecon_gui_before_release.PNG)

### キーボード操作  
キーボードをスイッチのコントローラとして使用することができます  

| Switchコントローラ | キーボード |
| ---- | ---- |
| A, B, X, Y, L, R | 'a', 'b', ...キー |
| ZL | 'k'キー |
| ZR | 'e'キー |
| MINUS | 'm'キー |
| PLUS | 'p'キー |
| LCLICK | 'q'キー |
| RCLICK | 'w'キー |
| HOME | 'h'キー |
| CAPTURE | 'c'キー |
| 左スティック | 矢印キー |

## リリース

- 過去リリース  
	- [Github - Releases](https://github.com/KawaSwitch/Poke-Controller/releases)  

- 進捗状況の確認  
	- [Github - Project](https://github.com/KawaSwitch/Poke-Controller/projects)  

- ロードマップ  
	- [リリースについて](https://github.com/KawaSwitch/Poke-Controller/wiki/About-Releases)  

## 貢献

これらの貢献者に感謝します ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/KawaSwitch"><img src="https://avatars3.githubusercontent.com/u/41296626?v=4" width="100px;" alt=""/><br /><sub><b>KawaSwitch</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=KawaSwitch" title="Code">💻</a> <a href="#maintenance-KawaSwitch" title="Maintenance">🚧</a> <a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=KawaSwitch" title="Documentation">📖</a> <a href="#question-KawaSwitch" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/Moi-poke"><img src="https://avatars1.githubusercontent.com/u/59233665?v=4" width="100px;" alt=""/><br /><sub><b>Moi-poke</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=Moi-poke" title="Code">💻</a> <a href="#question-Moi-poke" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/xv13"><img src="https://avatars2.githubusercontent.com/u/47322147?v=4" width="100px;" alt=""/><br /><sub><b>xv13</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/issues?q=author%3Axv13" title="Bug reports">🐛</a></td>
	<td align="center"><a href="https://github.com/vyPeony"><img src="https://avatars0.githubusercontent.com/u/39150264?v=4" width="100px;" alt=""/><br /><sub><b>vyPeony</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=vyPeony" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

このプロジェクトは, [all-contributors](https://github.com/all-contributors/all-contributors)仕様に準拠しています. どんな貢献も歓迎します！

## ライセンス

本プロジェクトはMITライセンスです  
詳細は [LISENCE](https://github.com/KawaSwitch/Poke-Controller/blob/master/LICENSE) を参照ください  

また, 本プロジェクトではLGPLライセンスのDirectShowLib-2005.dllを同梱し使用しています  
[About DirectShowLib](http://directshownet.sourceforge.net/)  
