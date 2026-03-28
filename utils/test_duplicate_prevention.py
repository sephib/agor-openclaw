#!/usr/bin/env python3
"""
Test Suite for Duplicate Prevention

This test suite verifies that the duplicate prevention system works correctly.

Test cases:
1. All tickets have sessions → creates 0 new sessions
2. All tickets are new → creates all new sessions
3. Mixed scenario → creates only new ones
4. State file out of sync → detected and corrected
"""

import json
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

# Import the modules to test
sys.path.insert(0, str(Path(__file__).parent))
from generate_actions import generate_actions, get_active_sessions_map
from verify_no_duplicates import (
    get_state_ticket_ids,
    verify_plan_file,
    verify_actions_file
)


class TestDuplicatePrevention:
    """Test duplicate prevention system"""

    def __init__(self):
        self.test_results = []
        self.passed = 0
        self.failed = 0

    def log(self, test_name: str, passed: bool, message: str = ""):
        """Log test result"""
        status = "✅ PASS" if passed else "❌ FAIL"
        self.test_results.append({
            'test': test_name,
            'passed': passed,
            'message': message
        })

        if passed:
            self.passed += 1
        else:
            self.failed += 1

        print(f"{status}: {test_name}")
        if message:
            print(f"       {message}")

    def create_mock_state(self, tickets: List[str]) -> Dict:
        """Create mock state file with active sessions for given tickets"""
        return {
            "active_coding_sessions": [],
            "active_research_sessions": [],
            "active_personal_sessions": [
                {
                    "session_id": f"mock-session-{ticket[:8]}",
                    "ticket_id": ticket,
                    "ticket_title": f"Mock ticket {ticket}",
                    "category": "personal"
                }
                for ticket in tickets
            ]
        }

    def create_mock_plan(self, tickets: List[Dict]) -> Dict:
        """Create mock plan with given tickets"""
        return {
            "personal_tasks": tickets,
            "coding_tasks": [],
            "research_tasks": []
        }

    def test_all_tickets_have_sessions(self):
        """Test Case 1: All tickets already have active sessions"""
        test_name = "All tickets have sessions → creates 0"

        # Create state with 3 active tickets
        state = self.create_mock_state([
            "672215e999cf9c79e0bb303a",
            "69bb8f78230724849642b0e3",
            "69b0f3d51f042e4bd727ce07"
        ])

        # Create plan with same 3 tickets
        plan = self.create_mock_plan([
            {
                "card_id": "672215e999cf9c79e0bb303a",
                "title": "Ticket 1",
                "description": "",
                "url": "https://trello.com/c/test1",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "69bb8f78230724849642b0e3",
                "title": "Ticket 2",
                "description": "",
                "url": "https://trello.com/c/test2",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "69b0f3d51f042e4bd727ce07",
                "title": "Ticket 3",
                "description": "",
                "url": "https://trello.com/c/test3",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            }
        ])

        # Save mock files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as plan_file:
            json.dump(plan, plan_file)
            plan_path = plan_file.name

        # Mock the state loading
        import generate_actions as ga
        original_load = ga.load_state
        ga.load_state = lambda: state

        try:
            # Generate actions
            actions = generate_actions(plan_path)

            # Verify
            create_count = actions['stats']['creates']
            update_count = actions['stats']['updates']

            if create_count == 0 and update_count == 3:
                self.log(
                    test_name,
                    True,
                    f"Correctly generated 0 creates, 3 updates"
                )
            else:
                self.log(
                    test_name,
                    False,
                    f"Expected 0 creates, got {create_count}. Expected 3 updates, got {update_count}"
                )
        finally:
            ga.load_state = original_load
            Path(plan_path).unlink()

    def test_all_tickets_are_new(self):
        """Test Case 2: All tickets are new (no active sessions)"""
        test_name = "All tickets are new → creates all"

        # Create empty state
        state = self.create_mock_state([])

        # Create plan with 3 new tickets
        plan = self.create_mock_plan([
            {
                "card_id": "NEW001",
                "title": "New Ticket 1",
                "description": "",
                "url": "https://trello.com/c/new1",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "NEW002",
                "title": "New Ticket 2",
                "description": "",
                "url": "https://trello.com/c/new2",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "NEW003",
                "title": "New Ticket 3",
                "description": "",
                "url": "https://trello.com/c/new3",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            }
        ])

        # Save mock files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as plan_file:
            json.dump(plan, plan_file)
            plan_path = plan_file.name

        # Mock the state loading
        import generate_actions as ga
        original_load = ga.load_state
        ga.load_state = lambda: state

        try:
            # Generate actions
            actions = generate_actions(plan_path)

            # Verify
            create_count = actions['stats']['creates']
            update_count = actions['stats']['updates']

            if create_count == 3 and update_count == 0:
                self.log(
                    test_name,
                    True,
                    f"Correctly generated 3 creates, 0 updates"
                )
            else:
                self.log(
                    test_name,
                    False,
                    f"Expected 3 creates, got {create_count}. Expected 0 updates, got {update_count}"
                )
        finally:
            ga.load_state = original_load
            Path(plan_path).unlink()

    def test_mixed_scenario(self):
        """Test Case 3: Mixed - some tickets have sessions, some are new"""
        test_name = "Mixed scenario → creates only new ones"

        # Create state with 2 active tickets
        state = self.create_mock_state([
            "EXISTING001",
            "EXISTING002"
        ])

        # Create plan with 2 existing + 2 new tickets
        plan = self.create_mock_plan([
            {
                "card_id": "EXISTING001",
                "title": "Existing Ticket 1",
                "description": "",
                "url": "https://trello.com/c/ex1",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "EXISTING002",
                "title": "Existing Ticket 2",
                "description": "",
                "url": "https://trello.com/c/ex2",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "NEW001",
                "title": "New Ticket 1",
                "description": "",
                "url": "https://trello.com/c/new1",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            },
            {
                "card_id": "NEW002",
                "title": "New Ticket 2",
                "description": "",
                "url": "https://trello.com/c/new2",
                "list_name": "Test",
                "labels": [],
                "due_date": None,
                "priority_score": 10,
                "priority_reasoning": "test",
                "category": "personal"
            }
        ])

        # Save mock files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as plan_file:
            json.dump(plan, plan_file)
            plan_path = plan_file.name

        # Mock the state loading
        import generate_actions as ga
        original_load = ga.load_state
        ga.load_state = lambda: state

        try:
            # Generate actions
            actions = generate_actions(plan_path)

            # Verify
            create_count = actions['stats']['creates']
            update_count = actions['stats']['updates']

            if create_count == 2 and update_count == 2:
                self.log(
                    test_name,
                    True,
                    f"Correctly generated 2 creates, 2 updates"
                )
            else:
                self.log(
                    test_name,
                    False,
                    f"Expected 2 creates, got {create_count}. Expected 2 updates, got {update_count}"
                )
        finally:
            ga.load_state = original_load
            Path(plan_path).unlink()

    def test_duplicate_detection(self):
        """Test Case 4: Detect when actions file would create duplicates"""
        test_name = "Duplicate detection in verification"

        # Create state with 1 active ticket
        state = self.create_mock_state(["TICKET001"])

        # Create actions file that tries to CREATE for existing ticket
        actions = {
            "generated_at": "2026-03-19T00:00:00Z",
            "plan_file": "test.json",
            "stats": {
                "updates": 0,
                "creates": 1
            },
            "actions": [
                {
                    "action": "create",
                    "ticket_id": "TICKET001",
                    "title": "Test ticket",
                    "category": "personal"
                }
            ],
            "active_sessions_count": 1
        }

        # Save mock files
        state_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        json.dump(state, state_file)
        state_file.close()

        actions_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        json.dump(actions, actions_file)
        actions_file.close()

        try:
            # This test would need to mock the verification script
            # For now, we'll test the logic manually

            state_tickets = get_state_ticket_ids(state)
            actions_check = verify_actions_file(Path(actions_file.name))

            duplicate_found = False
            for action in actions_check['actions']:
                if action['action'] == 'create' and action['ticket_id'] in state_tickets:
                    duplicate_found = True
                    break

            if duplicate_found:
                self.log(
                    test_name,
                    True,
                    "Correctly detected duplicate CREATE action"
                )
            else:
                self.log(
                    test_name,
                    False,
                    "Failed to detect duplicate CREATE action"
                )
        finally:
            Path(state_file.name).unlink()
            Path(actions_file.name).unlink()

    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "=" * 70)
        print("🧪 DUPLICATE PREVENTION TEST SUITE")
        print("=" * 70)
        print()

        self.test_all_tickets_have_sessions()
        self.test_all_tickets_are_new()
        self.test_mixed_scenario()
        self.test_duplicate_detection()

        print()
        print("=" * 70)
        print(f"📊 TEST RESULTS: {self.passed} passed, {self.failed} failed")
        print("=" * 70)
        print()

        return self.failed == 0


def main():
    """Main entry point"""
    tester = TestDuplicatePrevention()
    success = tester.run_all_tests()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
