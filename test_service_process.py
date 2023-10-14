import service_process


#
#
#

def test_should_remove_4_contigous_duplicates_reduce_15_char():
    input_string = "AAAc91%cWwWkLq$1ci3_848v3d__K"
    expected_result = ["Ac91%cWkLq£1ci3"]
    result = service_process.process_strings([input_string])
    print("Actual result:", result)
    print("Expected result:", expected_result)
    assert result == expected_result

if __name__ == "__main__":
    test_should_remove_4_contigous_duplicates_reduce_15_char()
    print("Test finished.")

