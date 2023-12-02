from YAMLparser import checkIfWeirdYAML, keyMiner, checkIfValidK8SYaml, checkIfValidHelm, readYAMLAsStr
import pytest
# Fuzzing Method 1: checkIfWeirdYAML
def test_checkIfWeirdYAML():
    # Test with valid YAML path
    assert checkIfWeirdYAML('/path/to/github/workflows/') == True

    # Test with invalid YAML path
    assert checkIfWeirdYAML('/path/to/regular/file.yaml') == False

# Fuzzing Method 2: keyMiner
def test_keyMiner():
    # Test with a simple dictionary
    dic_1 = {'a': {'b': {'c': 'value'}}}
    assert keyMiner(dic_1, 'value') == ['a', 'b', 'c']

    # Test with a different structure
    dic_2 = {'x': {'y': {'z': 'target'}}}
    assert keyMiner(dic_2, 'target') == ['x', 'y', 'z']

# Fuzzing Method 3: checkIfValidK8SYaml
def test_checkIfValidK8SYaml():
    # Test with a valid Kubernetes YAML
    assert checkIfValidK8SYaml('/path/to/valid/k8s.yaml') == True

    # Test with an invalid YAML
    assert checkIfValidK8SYaml('/path/to/invalid.yaml') == False

# Fuzzing Method 4: checkIfValidHelm
def test_checkIfValidHelm():
    # Test with a valid Helm path and value
    assert checkIfValidHelm('/path/to/helm.yaml') == True

    # Test with an invalid Helm path
    assert checkIfValidHelm('/path/to/regular/file.yaml') == False

# Fuzzing Method 5: readYAMLAsStr
def test_readYAMLAsStr():
    # Test with a valid YAML file
    assert isinstance(readYAMLAsStr('/path/to/valid/file.yaml'), str)

    # Test with an invalid YAML file
    assert isinstance(readYAMLAsStr('/path/to/invalid/file.txt'), str)


if __name__ == '__main__':
    pytest.main()