import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def generate_graphs():
    # Load Japanese font
    font_path = 'fonts/ipaexg.ttf'
    try:
        font_prop = fm.FontProperties(fname=font_path)
    except FileNotFoundError:
        print(f"Font not found at {font_path}")
        return

    # Graph 1: AR(1) Correlation Matrix Heatmap
    T = 10
    alpha = 0.5

    # Create correlation matrix
    # R[i, j] = alpha^|i-j|
    i, j = np.indices((T, T))
    correlation_matrix = alpha ** np.abs(i - j)

    plt.figure(figsize=(8, 6))
    im = plt.imshow(correlation_matrix, cmap='viridis')
    cbar = plt.colorbar(im)
    cbar.set_label(r'$\alpha^{|i-j|}$')

    plt.title(f'AR(1) 相関行列 (T={T}, alpha={alpha})\n帯は h=|i-j| (対角からの距離) に対応', fontproperties=font_prop)
    plt.xlabel('j')
    plt.ylabel('i')
    # Set ticks to integers
    plt.xticks(np.arange(0, T, 2))
    plt.yticks(np.arange(0, T, 2))

    plt.tight_layout()
    plt.savefig('ar_correlation_matrix.png')
    plt.close()
    print("Generated ar_correlation_matrix.png")

    # Graph 2: Precision loss from correlation
    # ratio = Var(y_T_bar) / Var(x_10_bar)
    # where x is IID with same process variance gamma_0

    alphas = [0.2, 0.5, 0.8]
    T_max = 100
    T_range = np.arange(1, T_max + 1)

    plt.figure(figsize=(10, 6))

    for alpha_val in alphas:
        ratios = []
        for t in T_range:
            if t == 1:
                sum_term = 0
            else:
                h = np.arange(1, t)
                sum_term = np.sum((t - h) * (alpha_val ** h))

            # The part inside brackets of variance formula
            var_term = t + 2 * sum_term

            # Ratio calculation
            # Var(y_bar_t) is proportional to var_term / t^2
            # Var(x_bar_10) is proportional to 1/10
            ratio = (var_term / (t**2)) / (1.0 / 10.0)
            ratios.append(ratio)

        plt.plot(T_range, ratios, label=f'alpha={alpha_val}')

    # Add reference lines
    plt.axhline(y=1.0, color='steelblue', linestyle='--', alpha=0.7)
    plt.axvline(x=10.0, color='steelblue', linestyle='--', alpha=0.7)

    plt.title('相関による精度の低下\nratio = Var($\\bar{y}_T$) / Var($\\bar{x}_{10}$)', fontproperties=font_prop)
    plt.xlabel('T (サンプルサイズ)', fontproperties=font_prop)
    plt.ylabel('ratio')
    plt.legend()
    plt.grid(False)

    plt.tight_layout()
    plt.savefig('ar_variance_ratio.png')
    plt.close()
    print("Generated ar_variance_ratio.png")

if __name__ == "__main__":
    generate_graphs()
