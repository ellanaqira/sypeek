import pytest
from unittest.mock import patch

from sypeek import opsy


def _mock_opsy_funct(mocker_plugin, func_name: str, mocked_value):
    mocker_plugin.patch(f"sypeek.{func_name}").return_value = mocked_value


# test opsy.opsy_kernel function ===============================
def test_mock_opsy_kernel(mocker):
    mocked_value: str = "mocked_kernel"
    _mock_opsy_funct(mocker, "opsy.opsy_kernel", mocked_value)
    assert opsy.opsy_kernel() == mocked_value

def test_exception_opsy_kernel():
    exception_msg: str = f"Couldn't get 'Kernel Name' information"

    with patch(f"sypeek.opsy.opsy_kernel", side_effect=opsy.OpSyInfoError(exception_msg)):
        with pytest.raises(opsy.OpSyInfoError) as excinfo:
            opsy.opsy_kernel()
        assert excinfo.value.message == exception_msg
