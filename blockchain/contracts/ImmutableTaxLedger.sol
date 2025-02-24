// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ImmutableTaxLedger {
    struct TaxRecord {
        bytes32 dataHash;
        bytes32 computationHash;
        bool complianceStatus;
        string aiModelVersion;
    }

    mapping(bytes32 => TaxRecord) public taxRecords;

    event TaxRecordAdded(bytes32 indexed recordId, bytes32 dataHash);

    function addTaxRecord(
        bytes32 recordId,
        bytes32 dataHash,
        bytes32 computationHash,
        bool complianceStatus,
        string memory aiModelVersion
    ) public {
        TaxRecord memory newRecord = TaxRecord(
            dataHash,
            computationHash,
            complianceStatus,
            aiModelVersion
        );
        taxRecords[recordId] = newRecord;
        emit TaxRecordAdded(recordId, dataHash);
    }

    function verifyTaxRecord(bytes32 recordId, bytes32 dataHash) public view returns (bool) {
        return taxRecords[recordId].dataHash == dataHash;
    }
}
