"""
Module Name: Gorle_AIDLC_Model.py
Author: Mahesh Gorle
Course: CSC505 - Principles of Software Development - Module2- Critical Thinking
Description: Simulation script for the YourLastName AIDLC Adaptive Model,
             demonstrating the evolution from classic SDLC to agent-driven systems.
"""

import json
import sys
from typing import Dict, List, NamedTuple


class AIDLCNode(NamedTuple):
    node_id: int
    phase_name: str
    operational_scope: str
    agent_responsibilities: List[str]
    context_feedback_loops: List[str]


class AIDLCEngine:
    def __init__(self, developer_lastname: str):
        self.framework_signature = f"{developer_lastname} AIDLC Adaptive Model"
        self.graph_nodes: Dict[int, AIDLCNode] = {}

    def initiate_topology_builder(self) -> None:
        """Prompts for and configures the automated lifecycle phase profiles."""
        print("=" * 80)
        print(f" INITIALIZING SYSTEM COMPILER: {self.framework_signature.upper()}")
        print("=" * 80)
        print("Input active agent roles to compile your AIDLC model configuration.\n")

        # Industry standard reference markers for modern AIDLC automation structures
        aidlc_reference_architecture = [
            ("AI Intent Inception Phase", ["Requirement Parsing", "Goal Modeling"], ["Node 3 (Refinement Link)", "Node 5 (Context Sync)"]),
            ("Context Elaboration & Ingestion", ["Context Mapping", "Legacy Code Indexing"], ["Node 4 (Schema Match)"]),
            ("Concurrent Agentic Construction", ["Automated Code Gen", "Simultaneous Testing"], ["Node 1 (Intent Reset)"]),
            ("Automated CI/CD Canary Deploy", ["IaC Generation", "Canary Route Scanning"], ["Node 2 (Pipeline Fix)"]),
            ("Runtime Telemetry & Context Store", ["Observability Tracking", "Memory Optimization"], ["Node 1 (Prompt Feed)", "Node 3 (Auto-Fix)"])
        ]

        for i, (default_phase, baseline_tasks, default_feedback) in enumerate(aidlc_reference_architecture, 1):
            print(f"--- [Compiling AIDLC Lifecycle Node {i} / 5] ---")
            user_phase_name = input(f"Enter structural name for Phase {i} [Default: '{default_phase}']: ").strip()
            phase_name = user_phase_name if user_phase_name else default_phase

            user_scope = input(f"Provide professional technical description for '{phase_name}': ").strip()
            if not user_scope:
                operational_scope = "Executes automated agent execution, continuous context assessment, and operational feedback cycles."
            else:
                operational_scope = user_scope

            self.graph_nodes[i] = AIDLCNode(
                node_id=i,
                phase_name=phase_name,
                operational_scope=operational_scope,
                agent_responsibilities=baseline_tasks,
                context_feedback_loops=default_feedback
            )
            print()

    def output_architectural_manifest(self) -> None:
        """Generates a complete system manifest detailing model topology."""
        if not self.graph_nodes:
            print("[CRITICAL ERROR] Configuration blueprint empty. Process halted.", file=sys.stderr)
            return

        print("\n" + "=" * 80)
        print(f" TECHNICAL ARCHITECTURE SPECIFICATION: {self.framework_signature.upper()}")
        print("=" * 80)
        print("Paradigm Context: Autonomous AI-Driven Development Lifecycle (AIDLC vs SDLC Class)")
        print("-" * 80)

        for nid, node in sorted(self.graph_nodes.items()):
            print(f"Lifecycle Node {node.node_id}: [{node.phase_name.upper()}]")
            print(f"  ├── Functional Mission Scope : {node.operational_scope}")
            print(f"  ├── Integrated Agent Actions : {', '.join(node.agent_responsibilities)}")
            print(f"  └── Active Context Loops    : {', '.join(node.context_feedback_loops)}")
            print("-" * 80)

        print("\n[SUCCESS] AIDLC pipeline topology schema compiled and verified successfully.")
        print("=" * 80)


def main():
    try:
        lastname_token = input("Enter your Last Name to initialize custom system signatures: ").strip()
        signature = lastname_token if lastname_token else "Architect"
        
        compiler_instance = AIDLCEngine(developer_lastname=signature)
        compiler_instance.initiate_topology_builder()
        compiler_instance.output_architectural_manifest()
    except (KeyboardInterrupt, SystemExit):
        print("\n\n[HALT] System compilation execution terminated by engineer.")
        sys.exit(0)


if __name__ == "__main__":
    main()
