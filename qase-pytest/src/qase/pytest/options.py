class QasePytestOptions:

    @staticmethod
    def addoptions(parser, group):
        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-mode",
            dest="qase_mode",
            help="Define Qase reporter mode: `off`, `report` or `testops`"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-environment",
            dest="qase_environment",
            help="Define environment slug or ID from TestOps"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-debug",
            dest="qase_debug",
            type="bool",
            help="Enable debug mode"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-execution-plan-path",
            dest="qase_execution_plan_path",
            help="Path to file with execution plan"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-project",
            dest="qase_testops_project",
            help="Project code in Qase TestOps"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-api-token",
            dest="qase_testops_api_token",
            help="API token for Qase TestOps"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-api-host",
            dest="qase_testops_api_host",
            help="API host for Qase TestOps"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-plan-id",
            dest="qase_testops_plan_id",
            help="Test Plan ID in Qase TestOps"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-run-id",
            dest="qase_testops_run_id",
            help="Test Run ID in Qase TestOps"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-run-title",
            "qase_testops_run_title",
            help="Define title for autocreated Test Run. If not set, will be used autogenerated title"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-run-description",
            dest="qase_testops_run_description",
            help="Define description for autocreated Test Run"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-run-complete",
            dest="qase_testops_run_description",
            type="bool",
            help="Complete run after tests execution"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-chunk",
            dest="qase_testops_chunk",
            help="Define batch size of results chunk. Default: 200."
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-testops-defect",
            dest="qase_testops_defect",
            type="bool",
            help="Create defect if test failed"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-report-driver",
            dest="qase_report_driver",
            help="Define report driver: `local`. More options coming soon."
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-report-connection-local-path",
            dest="qase_report_connection_local_path",
            help="Define local path for report directory"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-report-connection-local-format",
            dest="qase_report_connection_local_format",
            help="Define local format for report directory: `json` or `jsonp`"
        )

        QasePytestOptions.add_option(
            parser,
            group,
            "--qase-profilers",
            dest="qase_profilers",
            help="Profilers to use for tests. Available: `network`, `db`, `sleep`"
        )

    @staticmethod
    def add_option(parser, group, option, dest, default=None, type=None, **kwargs):
        # We are going to add options that were not added before through the manager
        try:
            group.addoption(option, dest=dest, default=default, action="store", **kwargs)
        except ValueError:
            pass
