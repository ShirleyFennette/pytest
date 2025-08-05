import allure
import pytest

@allure.id("63337")
@pytest.mark.example
@allure.feature("src/v3/abirvalg@")
@allure.story("Answering questionable questions")
@allure.title("Do stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammitDo stuff and then assert dammit")
@allure.issue("http://116.203.103.50:8080/projects/AL/issues/AL-5")
@allure.label("jira","AK-1")
@allure.testcase("60069")
def test_json_attach():
    with allure.step("define st1ff"):
        pass
    with allure.step("define stuff"):
        pass
    with allure.step("do stuff"):
        pass
    with allure.step("do more stuff"):
        pass
    with allure.step("do even more stuff"):
        pass
    with allure.step("expected result 2 < 3"):
        pass
        with allure.step("<b>asserting</b> 2 > 3"):
            assert(2 > 3)
