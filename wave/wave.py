import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 파동 방정식 변수 및 매개변수 설정
Lx = 10
dx = 0.1
nx = int(Lx / dx) + 1
x = np.linspace(0, Lx, nx)
T = 20
dt = 0.1
c = 1.0  # 파동 속도 (한 방향으로만 흐름)

# 파동 초기 조건 설정
wn = np.zeros(nx)
wni = []

# 소스 위치
source_pos = int(nx / 4)

# 시간 단계 설정
ts = np.arange(0, T + dt, dt)

# 소스 진폭 설정 (더 큰 진폭)
source_amplitude = 12.0

# 시간 스텝마다 파동 업데이트
for t in ts:
   wn[1:] = wn[1:] - c * (wn[1:] - wn[:-1]) * (dt / dx)
   wn[source_pos] += source_amplitude * np.sin(2 * np.pi * 10 * t / T) * (dt ** 2)

   wni.append(wn.copy())

# 애니메이션 설정
fig, ax = plt.subplots()
ax.set_xlim(0, Lx)
ax.set_ylim(-2, 2)  # 진폭을 크게 하려면 y 범위를 확장합니다.
line, = ax.plot([], [], 'b-')
source, = ax.plot([], [], 'ro')
txt = ax.text(5, 2.2, '', fontsize=15, color='g', ha='center', va='center')

def animate(i):
   line.set_data(x, wni[i])
   source.set_data(x[source_pos], wni[i][source_pos])
   txt.set_text(f'Time: {ts[i]:.1f}')
   return line, source

ani = animation.FuncAnimation(fig, animate, frames=len(wni), interval=10, repeat=False)
plt.show()
