# 第3章：RTL設計のAITL対応実務ポイント

## 🎯 本章の目的

本章では、FSM制御やPID信号処理など、PoCの動作を支えるRTL（Register Transfer Level）設計の実務的ポイントを示します。AITL構造を意識した状態制御・論理ブロック構成・シミュレーションフローに重点を置きます。

---

## 🧩 PoCにおけるRTLブロック例

| ブロック名         | 機能                                 | 接続先             |
|--------------------|--------------------------------------|--------------------|
| fsm_controller.v    | 状態遷移・イベント制御               | UART, 外部トリガ   |
| pid_logic.v         | 誤差演算と出力計算                   | ADC, PWMブロック   |
| uart_interface.v    | 外部コマンド入力・ログ出力           | 上位SoC            |
| top_poc.v           | 上記モジュールのトップ統合           | FPGA, SoC          |

---

## 🔧 RTLにおけるFSM記述の基本形

AITL構想では、人間の本能レベルの行動をFSMとして記述します。以下はその典型的な記述例です：

```verilog
always @(posedge clk or negedge rst_n) begin
  if (!rst_n) begin
    state <= IDLE;
  end else begin
    case (state)
      IDLE:
        if (start) state <= MOVE;
      MOVE:
        if (done)  state <= IDLE;
      default:
        state <= IDLE;
    endcase
  end
end
```

	•	IDLE, MOVE などは状態記号
	•	外部入力やセンサ条件によって状態遷移

## 🧠 AITL構造とのマッピング

| AITL層     | RTL構成例           | 説明                                 |
|------------|----------------------|--------------------------------------|
| 本能（FSM） | `fsm_controller.v`    | 状態記述・トリガ管理                 |
| 理性（PID） | `pid_logic.v`         | 制御量演算、目標値との差分制御       |
| 実行層     | `pwm_driver.v` 等     | PWM生成、DAC制御などのハード出力部   |

---

## 🧪 シミュレーション観点の設計ポイント

RTL設計段階でのPoC検証には、以下のような観点が有効です：

- **状態遷移ログ出力**（`$display` で状態遷移確認）
- **入力刺激の自動化**（テストベンチ内でシナリオ再現）
- **PID誤差の定量出力**（デバッグ信号に制御量出力）

```verilog
$display("State: %s, Error: %d, Output: %d", state, error, output_val);
```

## 📄 ソース分割と命名規約の一例

| ファイル名              | 内容                     |
|-------------------------|--------------------------|
| `fsm_controller.v`      | FSM本体                  |
| `pid_logic.v`           | PID演算部                |
| `uart_interface.v`      | UART制御                 |
| `top_poc.v`             | 統合モジュール           |
| `tb_top_poc.v`          | テストベンチ             |

---

## 🧰 RTL実装時のチェックリスト（抜粋）

- [ ] 入出力信号のレベル定義（active-high/low）明確か  
- [ ] 状態数・遷移パスが仕様と整合しているか  
- [ ] 制御信号が冗長になっていないか（過剰if文など）  
- [ ] シミュレーション波形で論理誤動作がないか  
- [ ] UARTやPWM等の周辺ブロックと接続整合しているか

---

## 📬 連絡先

執筆・設計：**三溝 真一（Shinichi Samizo）**  
GitHub: [https://github.com/Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com
