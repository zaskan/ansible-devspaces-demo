from unittest.mock import patch

# Replace 'sample_namespace.sample_collection.plugins.modules.hello_module'
# with the actual import path to your module.
@patch("sample_namespace.sample_collection.plugins.modules.hello_module.AnsibleModule")
def test_hello_module_main(mock_ansible_module):
    # Setup mock
    instance = mock_ansible_module.return_value
    instance.params = {"name": "World"}

    # Import your module under test
    from sample_namespace.sample_collection.plugins.modules import hello_module

    # Run the main function
    hello_module.main()

    # Check expected behavior
    instance.exit_json.assert_called_once_with(changed=False, message="Hello, World!")
