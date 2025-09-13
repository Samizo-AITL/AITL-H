# 9. 図

## 図1. AITLアーキテクチャの概念図
```tikz
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=1.2cm, auto]
  % PID
  \node[draw, rectangle, rounded corners, fill=blue!15, minimum width=3cm, minimum height=1cm] (pid) {PID制御層};

  % FSM
  \node[draw, rectangle, rounded corners, fill=green!15, below=of pid, minimum width=3cm, minimum height=1cm] (fsm) {FSMモード監督層};

  % LLM
  \node[draw, rectangle, rounded corners, fill=orange!20, below=of fsm, minimum width=3cm, minimum height=1cm] (llm) {LLM適応層};

  % Arrows
  \draw[->, thick] (pid) -- (fsm);
  \draw[->, thick] (fsm) -- (llm);
\end{tikzpicture}
\caption{三層構造によるAITLアーキテクチャ}
\end{figure}
```

---

## 図2. 22nm FD-SOI SoC設計とチップレット統合
```tikz
\begin{figure*}[h]
\centering
\begin{tikzpicture}[node distance=1.5cm, auto]

  % SoC Core
  \node[draw, rectangle, rounded corners, fill=blue!20, minimum width=4cm, minimum height=1.2cm] (core) {22nm FD-SOI Core SoC};

  % Memory Blocks
  \node[draw, rectangle, fill=yellow!20, below left=1cm and 2cm of core, minimum width=2.5cm, minimum height=1cm] (sram) {SRAM (低遅延)};
  \node[draw, rectangle, fill=purple!20, below=1cm of core, minimum width=2.5cm, minimum height=1cm] (mram) {MRAM (不揮発)};
  \node[draw, rectangle, fill=red!20, below right=1cm and 2cm of core, minimum width=2.5cm, minimum height=1cm] (fram) {FRAM (耐放射線)};

  % Chiplet Interconnect
  \node[draw, rectangle, dashed, fill=gray!10, above=1.5cm of core, minimum width=6cm, minimum height=1cm] (interposer) {Chiplet Interposer / NoC};

  % Arrows
  \draw[<->, thick] (core) -- (sram);
  \draw[<->, thick] (core) -- (mram);
  \draw[<->, thick] (core) -- (fram);
  \draw[<->, thick] (core) -- (interposer);

\end{tikzpicture}
\caption{22nm FD-SOIベースSoCとチップレット統合アーキテクチャ}
\end{figure*}
```

---

## 図3. H∞多次元制御による外乱抑制
```tikz
\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1.0, node distance=1.5cm, auto]
  % Plant
  \node[draw, rectangle, fill=green!15, minimum width=2.8cm, minimum height=1cm] (plant) {対象システム};

  % Controller
  \node[draw, rectangle, fill=blue!15, left=3cm of plant, minimum width=2.8cm, minimum height=1cm] (controller) {H∞ 多次元制御器};

  % Disturbance
  \node[draw, circle, fill=red!20, above=1.5cm of plant] (disturbance) {外乱};

  % Arrows
  \draw[->, thick] (controller) -- (plant) node[midway, above] {制御入力};
  \draw[->, thick] (disturbance) -- (plant);
  \draw[->, thick] (plant.east) -- ++(1.5,0) node[right] {出力応答};
\end{tikzpicture}
\caption{H∞多次元制御による外乱抑制の概念図}
\end{figure}
```
