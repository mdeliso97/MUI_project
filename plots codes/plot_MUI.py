from confidence_interval import *
from matplotlib import pyplot as plt
from scipy import stats


def data_plot():

    x_labels = ["user0", "user1", "user2", "user3", "user4", "user5"]
    y_labels_unimodal_time = [33.00, 61.00, 26.00, 48.00, 69.00, 21.0]
    y_labels_multimodal_time = [42.01, 55.00, 28.05, 45.00, 39.00, 28.00]
    y_labels_unimodal_errors = [1, 15, 5, 10, 10, 5]
    y_labels_multimodal_errors = [0, 12, 5, 8, 8, 5]

    lw_bound, up_bound, margin_of_error, mean = confidence_interval(data=y_labels_multimodal_time,
                                                                    confidence=1.96)

    plt.plot(x_labels, y_labels_multimodal_time, label="time multi-modal", color="blue")
    plt.hlines(mean, xmin=0, xmax=len(x_labels), color='blue', linestyles='dashed')


    lw_bound, up_bound, margin_of_error, mean = confidence_interval(data=y_labels_unimodal_time,
                                                                    confidence=1.96)

    plt.plot(x_labels, y_labels_unimodal_time, label="time uni-modal", color="green")
    plt.hlines(mean, xmin=0, xmax=len(x_labels), color='green', linestyles='dashed')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=11)

    plt.xlabel("Users")
    plt.ylabel("Runtime (seconds)")
    plt.title(f"Runtime tasks sequence execution")
    plt.subplots_adjust(bottom=0.2, top=0.9)

    plt.savefig('Runtime_MUI.png')
    plt.show()
    plt.close()

    # Error rate plot
    lw_bound, up_bound, margin_of_error, mean = confidence_interval(data=y_labels_multimodal_errors,
                                                                    confidence=1.96)

    plt.plot(x_labels, y_labels_multimodal_errors, label="errors multi-modal", color="blue")
    plt.hlines(mean, xmin=0, xmax=len(x_labels), color='blue', linestyles='dashed')

    lw_bound, up_bound, margin_of_error, mean = confidence_interval(data=y_labels_unimodal_errors,
                                                                    confidence=1.96)

    plt.plot(x_labels, y_labels_unimodal_errors, label="errors uni-modal", color="green")
    plt.hlines(mean, xmin=0, xmax=len(x_labels), color='green', linestyles='dashed')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=11)

    plt.xlabel("Users")
    plt.ylabel("Error count")
    plt.title(f"Error count on tasks sequence execution")
    plt.subplots_adjust(bottom=0.2, top=0.9)

    plt.savefig('errors_MUI.png')
    plt.show()
    plt.close()

    # Perform the t-test on time labels
    t_statistic, p_value = stats.ttest_ind(y_labels_unimodal_time, y_labels_multimodal_time)

    # Print the results
    print("T-Statistic time: ", t_statistic)
    print("P-Value time: ", p_value)

    # Perform the t-test on error count labels
    t_statistic, p_value = stats.ttest_ind(y_labels_unimodal_errors, y_labels_multimodal_errors)

    # Print the results
    print("T-Statistic errors: ", t_statistic)
    print("P-Value errors: ", p_value)












if __name__ == "__main__":
    data_plot()