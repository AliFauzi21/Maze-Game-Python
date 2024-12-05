# Ａ－１）別ファイルから、マップ情報等すべてをインポート
# Ａ－１）※定数名などが重複しないように注意
from mazemap import *
# Ａ－２）tkinterのインポート
import tkinter
# Ａ－３）tkinterのメッセージボックスのインポート
from tkinter import messagebox
# Ｂ－１１）迷路のマップを設定
maze_map = MAZE_MAP_1
# Ｂ－１２）自キャラの初期位置を一旦変数に入れる
my_pos = START_POS_1
# Ｂ－１３）自キャラの位置（初期位置を設定）
my_x, my_y = my_pos
# Ａ－４）ウィンドウオブジェクトの作成
root = tkinter.Tk()
# Ａ－５）ウィンドウタイトルの設定「迷路塗りゲーム」
root.title('迷路塗りゲーム')
# Ａ－６）ウィンドウサイズの設定
root.geometry('800x560')
# Ａ－７）ウィンドウのサイズ変更の抑制
root.resizable(False, False)
# Ａ－８）キャンバスの作成
canvas = tkinter.Canvas(width=800, height=560, bg='white')
# Ａ－９）キャンバスの配置
canvas.place(x=0, y=0)

# Ｅ－３９）画面に四角ブロックを表示する関数
# Ｅ－４０）引数はx方向の位置、y方向の位置、色
def put_block(x, y, color):
    # Ｅ－４１）キャンバスに四角形を描画する（タグを指定）
    canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79,
                            fill=color, width=0, tag='BLOCK')
# Ｅ－４２）塗ってない残りのマス数（初期値は０）
nokori_count = 0
# Ｅ－４３）マップに合わせて、青ブロックを配置する
# Ｅ－４４）行数分の繰り返し
for y in range(7):
    # Ｅ－４５）列数分の繰り返し
    for x in range(10):
        # Ｅ－４６）該当マップ箇所のデータをチェック
        if maze_map[y][x] == 1:
            # Ｅ－４７）１なら青色ブロックを表示      
            put_block(x, y, 'skyblue')
        else:
            # Ｅ－４８）１以外なら、塗ってない残りのマス数を１加算
            nokori_count += 1

# Ｂ－１４）自キャラの画像ファイルを読み込み
my_img = tkinter.PhotoImage(file='image/cat.png')
# Ｂ－１５）自キャラを画面に表示（タグを設定）
canvas.create_image(my_x * 80, my_y * 80, image=my_img,
                    anchor='nw', tag='MY')

# Ｃ－２１）キー入力値（初期値は空）
key = ''
# Ｃ－２２）キーが押された時の処理
def key_down(e):
    # Ｃ－２３）キー入力値を更新できるようにする
    global key
    # Ｃ－２４）押されたキーを保持しておく
    key = e.keysym
    # Ｃ－２５）デバッグ用にターミナルに出力
    print('key_down', key)
# Ｃ－２６）キーが離された時の処理（押されたキーを破棄）
def key_up(e):
    # Ｃ－２７）キー入力値を更新できるようにする
    global key
    # Ｃ－２８）押されたキーの情報を空にする
    key = ''
    # Ｃ－２９）デバッグ用にターミナルに出力
    print('key_up')

# Ｃ－３０）キープレスイベントと関数をバインド
root.bind('<KeyPress>', key_down)
# Ｃ－３１）キーリリースイベントと関数をバインド
root.bind('<KeyRelease>', key_up)

# Ｂ－１６）メイン処理（この関数が繰り返し実行される）
def main_proc():
    # Ｄ－３２）キャラの位置、残りのマス数、キー入力値更新できるようにする
    global my_x, my_y, nokori_count, key
    
    # Ｉ－５８）左シフトキーが押された時
    
        # Ｉ－５９）キー入力値を空にする
        
        # Ｉ－６０）やり直すかのメッセージを出す
        # 「やり直し」「ゲームを最初からやり直しますか？」
        
        # Ｉ－６１）OKが押された場合
        
            # Ｉ－６２）ブロックをすべて消す
            
            # Ｉ－６３）自キャラの初期位置を戻す
            
            # Ｉ－６４）残りマス数を一度０に
            
            # Ｉ－６５）マップのマス分繰り返す
            
                
                    # Ｉ－６６）該当箇所が壁だったらブロックを表示
                    
                    
                    # Ｉ－６７）該当箇所が塗り済みだったら空白状態に戻す
                    
                    
                    # Ｉ－６８）該当箇所が空白だったら残りのマス数を１加算
                    
                    
                    
    
    # Ｄ－３３）今回のループで動かすマス数（縦、横）に初期値０を設定
    dx, dy = 0, 0
    # Ｄ－３４）各キーが押されてた時に、動かすマス数を設定する
    # Ｆ－４９）その方向の行き先にブロックがある場合移動しない
    if key == 'Down' and maze_map[my_y+1][my_x] == 0:
        dy = 1
    elif key == 'Up' and maze_map[my_y-1][my_x] == 0:
        dy = -1
    elif key == 'Right' and maze_map[my_y][my_x+1] == 0:
        dx = 1
    elif key == 'Left' and maze_map[my_y][my_x-1] == 0:
        dx = -1
    # Ｄ－３５）動かすマス数分、位置を変える
    my_x += dx
    my_y += dy
    # Ｇ－５０）自キャラの現在位置が空白なら
    if maze_map[my_y][my_x] == 0:
        # Ｇ－５１）マップの現在位置の数字を2にする
        maze_map[my_y][my_x] = 2
        # Ｇ－５２）ピンクのブロックを配置
        put_block(my_x, my_y, 'pink')
        # Ｇ－５３）残りのマス数を１減算
        nokori_count -= 1
    
    # Ｂ－１７）自キャラを一度消去（タグを指定）
    canvas.delete('MY')
    # Ｂ－１８）自キャラの画像を表示（移動していた処理から変更）
    canvas.create_image(my_x * 80, my_y * 80, image=my_img,
                        anchor='nw', tag='MY')
    # Ｈ－５４）残りのマス数が０になったら
    
        # Ｈ－５６）キャンバスを更新
        
        # Ｈ－５７）クリアメッセージを表示
        # 「おめでとう！」「すべての床を塗りました！」
        
    # Ｈ－５５）そうでない場合
    
    # Ｄ－３６）このループ中に移動したかチェック
    if dx == 0 and dy == 0:
        # Ｄ－３７）移動していない場合、すぐに次のメイン処理を繰り返す
        root.after(50, main_proc)
    else:
        # Ｄ－３８）移動した場合、少し待って、次のメイン処理を繰り返す
        # Ｂ－１９）次のメイン処理を繰り返す
        root.after(250, main_proc)

# Ｂ－２０）メイン処理の実行
main_proc()
# Ａ－１０）ウィンドウの表示
root.mainloop()
