from resources.handle_requests import HandleRequests
import filecmp

class Test:
    def run_testcases(self):
        for i in range(1,19):
            print("------------------------------------------------------------------")
            print('Testing testcase:', i)
            print(HandleRequests().handle_requests("test/input/t_c_"+str(i),"/test/output/t_c_"+str(i)+".txt"))
            if self.check_output("test/ideal_output/t_c_"+str(i)+".txt","test/output/t_c_"+str(i)+".txt"):
                print("Testcase", i, "Passed")
            else: print("Testcase", i, "failed")

    def check_output(self, ideal_file, output_file):
        return filecmp.cmp(ideal_file,output_file)

Test().run_testcases()